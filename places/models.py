from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.TextField(null=True, blank=True, verbose_name='Короткое описание')
    description_long = HTMLField(verbose_name='Полное описание')
    longitude = models.FloatField(verbose_name='Долгота местоположения')
    latitude = models.FloatField(verbose_name='Широта местоположения')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class PlaceImage(models.Model):
    image = models.ImageField(verbose_name='Изображение',blank=True,null=True)
    number = models.PositiveIntegerField(verbose_name='Номер изображения')
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='images', verbose_name='Место')

    def __str__(self):
        return self.place.title

    class Meta:
        ordering = ['number']
