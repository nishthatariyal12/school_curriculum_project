# Generated by Django 3.1.4 on 2021-04-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='user_type',
            field=models.CharField(choices=[('teacher', 'teacher'), ('student', 'student')], default='student', max_length=10),
        ),
    ]
