# Generated by Django 4.2.5 on 2023-10-24 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_alter_place_options_alter_placeimage_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='description_long',
            new_name='long_description',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='description_short',
            new_name='short_description',
        ),
    ]
