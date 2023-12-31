# Generated by Django 4.2.5 on 2023-10-26 12:26

from django.db import migrations


def copy_place_to_placedouble(apps, schema_editor):
    Place = apps.get_model('places', 'Place')
    PlaceDouble = apps.get_model('places', 'PlaceDouble')
    places = Place.objects.all()
    for place in places.iterator():
        PlaceDouble.objects.get_or_create(
            title=place.title,
            short_description=place.short_description,
            long_description=place.long_description,
            longitude=place.longitude,
            latitude=place.latitude
        )


class Migration(migrations.Migration):
    dependencies = [
        ('places', '0019_placedouble'),
    ]

    operations = [
        migrations.RunPython(copy_place_to_placedouble),
    ]
