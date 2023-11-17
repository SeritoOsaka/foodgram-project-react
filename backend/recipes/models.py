from colorfield.fields import ColorField
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models
from .validators import name_validator, color_validator
from users.models import User

from .constants import (MAX_COOKING_TIME, MAX_ING_AMOUNT, MIN_COOKING_TIME,
                        MIN_ING_AMOUNT, NAME_LIMIT, NAME_MAX_LENGTH,
                        COLOR_MAX_LENGTH)


class Ingredient(models.Model):
    name = models.CharField(
        'Название',
        max_length=NAME_MAX_LENGTH,
        validators=[name_validator],
    )
    measurement_unit = models.CharField(
        'Единицы измерения',
        max_length=NAME_MAX_LENGTH,
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('pk',)
        constraints = [
            models.UniqueConstraint(fields=['name', 'measurement_unit'],
                                    name='unique_name_measurement_unit')
        ]

    def __str__(self):
        return self.name[:NAME_LIMIT]


class Tag(models.Model):
    name = models.CharField(
        'Название',
        unique=True,
        max_length=NAME_MAX_LENGTH,
        validators=[color_validator],
    )
    color = ColorField(
        'Цвет',
        default='#FF0000',
        max_length=COLOR_MAX_LENGTH,
        unique=True,
        validators=[RegexValidator(regex='^#([A-Fa-f0-9]{3,6})$',
                                   message='Введите цвет в формате HEX')],
    )
    slug = models.SlugField(
        'Уникальный слаг',
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name',)

    def __str__(self):
        return self.name[:NAME_LIMIT]


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор',
    )
    name = models.CharField(
        'Название',
        max_length=NAME_MAX_LENGTH,
    )
    image = models.ImageField(
        'Картинка',
        upload_to='recipes/images/',
    )
    text = models.TextField(
        'Описание',
    )
    ingredients = models.ManyToManyField(
        verbose_name="Ингредиенты блюда",
        related_name="recipes",
        to=Ingredient,
        through="recipes.IngredientRecipe",
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
    )
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления',
        validators=[
            MinValueValidator(
                MIN_COOKING_TIME,
                message='Слишком быстро'
            ),
            MaxValueValidator(
                MAX_COOKING_TIME,
                message='Слишком долго'
            )
        ],
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'text'],
                name='unique_recipe'
            ),
        ]

    def __str__(self):
        return self.name[:NAME_LIMIT]


class IngredientRecipe(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='+',
        verbose_name='Рецепт',
    )
    amount = models.PositiveSmallIntegerField(
        'Количество в рецепте',
        validators=[
            MinValueValidator(
                MIN_ING_AMOUNT,
                message='Нужно указать нормальное количество!'
            ),
            MaxValueValidator(
                MAX_ING_AMOUNT,
                message='Кол-во ингредиентов не должно превышать 5000!'
            )
        ],
    )

    def __str__(self):
        return f'{self.ingredient} {self.recipe}'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Изб. рецепт',
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        unique_together = ['user', 'recipe']

    def __str__(self):
        return f'{self.user} {self.recipe}'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Изб. рецепт',
    )

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Списки покупок'
        unique_together = ['user', 'recipe']

    def __str__(self):
        return f'{self.user} {self.recipe}'
