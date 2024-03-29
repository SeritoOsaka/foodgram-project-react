# Generated by Django 3.2.3 on 2023-11-17 18:32

import colorfield.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_ingredient_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient_quantities',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', through='recipes.IngredientRecipe', to='recipes.Ingredient', verbose_name='Ингредиенты блюда'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=7, samples=None, unique=True, validators=[django.core.validators.RegexValidator(message='Введите цвет в формате HEX', regex='^#([A-Fa-f0-9]{3,6})$')], verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_color', message='Введите цвет в формате HEX.', regex='^#([A-Fa-f0-9]{3,6})$')], verbose_name='Название'),
        ),
    ]
