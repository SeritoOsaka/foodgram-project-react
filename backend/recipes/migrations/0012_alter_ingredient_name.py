# Generated by Django 3.2.3 on 2023-11-19 07:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_auto_20231119_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Эти данные могут содержать только буквы и пробелы.', regex='^[a-zA-Zа-яА-ЯёЁ]+$')], verbose_name='Название'),
        ),
    ]