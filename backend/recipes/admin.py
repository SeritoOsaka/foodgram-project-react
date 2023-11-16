from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet

from .models import (Favorite, Ingredient, IngredientRecipe, Recipe,
                     ShoppingCart, Tag)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'measurement_unit'
    )
    list_filter = ('name',)


class IngredientRecipeForm(BaseInlineFormSet):

    def clean(self):
        super(IngredientRecipeForm, self).clean()
        for form in self.forms:
            if not hasattr(form, 'cleaned_data'):
                continue
            data = form.cleaned_data
            if data.get('DELETE'):
                raise ValidationError(
                    'Нельзя удалять все ингредиенты из рецепта даже в админке!'
                )


class IngredientRecipeInLine(admin.TabularInline):
    model = IngredientRecipe
    min_num = 1
    formset = IngredientRecipeForm


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'color',
        'slug'
    )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'author',
        'count_favorite'
    )
    list_filter = ('author', 'tags')
    search_fields = ('name',)
    inlines = (IngredientRecipeInLine,)

    def count_favorite(self, obj):
        return obj.favorites.count()


admin.site.register(Favorite)
admin.site.register(ShoppingCart)
