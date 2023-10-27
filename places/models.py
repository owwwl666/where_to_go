from django.db import models

from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название',
        unique=True
    )
    short_description = models.TextField(
        verbose_name='Короткое описание',
        blank=True,
        default=''
    )
    long_description = HTMLField(
        verbose_name='Полное описание',
        blank=True,
        default=''
    )
    longitude = models.FloatField(verbose_name='Долгота местоположения')
    latitude = models.FloatField(verbose_name='Широта местоположения')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class PlaceImage(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    number = models.PositiveIntegerField(
        verbose_name='Номер изображения',
        blank=True,
        default=0,
        db_index=True
    )
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место'
    )

    def __str__(self):
        return self.place.title

    class Meta:
        ordering = ['number']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
