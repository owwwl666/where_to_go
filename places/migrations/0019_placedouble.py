# Generated by Django 4.2.5 on 2023-10-26 12:25

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0018_auto_20231025_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceDouble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Название')),
                ('short_description', models.TextField(blank=True, verbose_name='Короткое описание')),
                ('long_description', tinymce.models.HTMLField(blank=True, verbose_name='Полное описание')),
                ('longitude', models.FloatField(verbose_name='Долгота местоположения')),
                ('latitude', models.FloatField(verbose_name='Широта местоположения')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
                'ordering': ['title'],
            },
        ),
    ]
