# Generated by Django 5.0.6 on 2024-05-14 09:56

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_alter_room_description_alter_room_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(max_length=24, unique=True, validators=[core.validators.validate_slug]),
        ),
    ]
