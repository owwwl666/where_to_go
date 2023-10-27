from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

import requests

from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = ("Скачивает json файл с данными о конкретной локации на карте "
            "и сохраняет информацию в базу данных.")

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            type=str,
            help="URL адрес JSON файла для скачивания."
        )

    def handle(self, *args, **kwargs):
        url = kwargs['url']

        response = requests.get(url)
        payload = response.json()

        images_url = payload.get('imgs')
        title = payload.get('title')

        place, _ = Place.objects.get_or_create(
            title=title,
            defaults={
                'short_description': payload.get('description_short'),
                'long_description': payload.get('description_long'),
                'longitude': payload.get('coordinates').get('lng'),
                'latitude': payload.get('coordinates').get('lat')
            }
        )

        for image_number, image_url in enumerate(images_url):
            response = requests.get(image_url)
            image = response.content
            image_name = f'{title}_{image_number}.jpg'

            place_image, _ = PlaceImage.objects.get_or_create(
                image=ContentFile(image, name=image_name),
                number=image_number,
                place=place
            )
