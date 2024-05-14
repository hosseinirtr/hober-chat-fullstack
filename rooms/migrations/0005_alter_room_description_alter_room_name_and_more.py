# Generated by Django 5.0.6 on 2024-05-14 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_room_is_private_room_members_alter_message_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(max_length=128),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=24),
        ),
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(max_length=24, unique=True),
        ),
    ]
