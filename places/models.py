from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.TextField(null=True, blank=True, verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Полное описание')
    longitude = models.FloatField(verbose_name='Долгота местоположения')
    latitude = models.FloatField(verbose_name='Широта местоположения')

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    number = models.PositiveIntegerField(verbose_name='Номер изображения')
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='places', verbose_name='Место')
