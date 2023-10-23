from django.core.management.base import BaseCommand
import requests
from places.models import Place, PlaceImage
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = "Скачивает json файл с данными о конкретной локации на карте и сохраняет информацию в базу данных."

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help="URL адрес JSON файла для скачивания.")

    def handle(self, *args, **kwargs):
        def get_or_create_place_in_database(title, description_short, description_long, longitude,
                                            latitude):
            """Создает локацию в базе данных либо получает из нее, если локация уже создана."""
            place, _ = Place.objects.get_or_create(
                title=title,
                description_short=description_short,
                description_long=description_long,
                longitude=longitude,
                latitude=latitude
            )
            return place

        def get_or_create_images_in_database(image, image_name, image_number):
            """Сохраняет в базу данных все картинки выбранной локации."""
            place = get_or_create_place_in_database(title, description_short, description_long, longitude,
                                                    latitude)
            place_image, _ = PlaceImage.objects.get_or_create(number=image_number, place=place)
            place_image.image.save(image_name, content=ContentFile(image), save=True)

        url = kwargs['url']

        response = requests.get(url)
        place_data = response.json()

        title = place_data.get('title')
        description_short = place_data.get('description_short')
        description_long = place_data.get('description_long')
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
