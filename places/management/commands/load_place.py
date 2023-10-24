from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

import requests

from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = "Скачивает json файл с данными о конкретной локации на карте и сохраняет информацию в базу данных."

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help="URL адрес JSON файла для скачивания.")

    def handle(self, *args, **kwargs):
        def get_or_create_place_in_database(title, short_description, long_description, longitude,
                                            latitude):
            """Создает локацию в базе данных либо получает из нее, если локация уже создана."""
            place, _ = Place.objects.get_or_create(
                title=title,
                short_description=short_description,
                long_description=long_description,
                longitude=longitude,
                latitude=latitude
            )
            return place

        def get_or_create_images_in_database(image, image_name, image_number):
            """Сохраняет в базу данных все картинки выбранной локации."""
            place = get_or_create_place_in_database(title, short_description, long_description, longitude,
                                                    latitude)
            place_image, _ = PlaceImage.objects.get_or_create(number=image_number, place=place)
            place_image.image.save(image_name, content=ContentFile(image), save=True)

        url = kwargs['url']

        response = requests.get(url)
        place_data = response.json()

        title = place_data.get('title')
        short_description = place_data.get('short_description')
        long_description = place_data.get('long_description')
        longitude = place_data.get('coordinates').get('lng')
        latitude = place_data.get('coordinates').get('lat')
        images_url = place_data.get('imgs')

        for image_number, image_url in enumerate(images_url):
            response = requests.get(image_url)
            image = response.content
            image_name = f'{title}_{image_number}.jpg'

            get_or_create_images_in_database(
                image=image,
                image_name=image_name,
                image_number=image_number
            )
