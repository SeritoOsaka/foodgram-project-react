import csv

from django.core.management import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        file_path = 'data/ingredients.csv'
        try:
            with open(file_path, encoding='UTF-8') as file:
                ingredients_list = []
                for row in csv.reader(file):
                    name, measurement_unit = row
                    ingredient = Ingredient(name=name,
                                            measurement_unit=measurement_unit)
                    ingredients_list.append(ingredient)

                Ingredient.objects.bulk_create(ingredients_list)
                print('Импорт данных завершен!')
        except FileNotFoundError:
            print(f'File not found: {file_path}')
        except Exception as error:
            print(f'An error occurred: {error}')
