# Generated by Django 3.1.4 on 2021-04-16 15:17

import basic_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20210416_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to=basic_app.models.path_and_rename, verbose_name='profile_picture'),
        ),
    ]
