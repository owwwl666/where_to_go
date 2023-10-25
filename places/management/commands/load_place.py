from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

import requests

from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = "Скачивает json файл с данными о конкретной локации на карте и сохраняет информацию в базу данных."

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help="URL адрес JSON файла для скачивания.")

    def handle(self, *args, **kwargs):
        def get_or_create_images_in_database(image, image_name, image_number, place):
            """Сохраняет в базу данных все картинки выбранной локации."""
            place_image, _ = PlaceImage.objects.get_or_create(image=ContentFile(image, name=image_name),
                                                              number=image_number,
                                                              place=place)

        url = kwargs['url']

        response = requests.get(url)
        place_data = response.json()

        images_url = place_data.get('imgs')
        title = place_data.get('title')

        place, _ = Place.objects.get_or_create(
            title=title,
            defaults={
                'short_description': place_data.get('description_short'),
                'long_description': place_data.get('description_long'),
                'longitude': place_data.get('coordinates').get('lng'),
                'latitude': place_data.get('coordinates').get('lat')
            }
        )

        for image_number, image_url in enumerate(images_url):
            response = requests.get(image_url)
            image = response.content
            image_name = f'{title}_{image_number}.jpg'

            get_or_create_images_in_database(
                image=image,
                image_name=image_name,
                image_number=image_number,
                place=place
            )
