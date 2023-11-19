# Generated by Django 3.2.3 on 2023-11-19 07:25

import colorfield.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_alter_ingredient_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Имя и Фамилия могут содержать только буквы и пробелы.', regex='^[a-zA-Zа-яА-ЯёЁ]+$')], verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=7, samples=None, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_color', message='Введите цвет в формате HEX.', regex='^#([A-Fa-f0-9]{3,6})$')], verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название'),
        ),
    ]
