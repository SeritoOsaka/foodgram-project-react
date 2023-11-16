import csv

from django.core.management import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        file_path = 'data/ingredients.csv'

        try:
            with open(file_path, encoding='UTF-8') as file:
                ingredients_to_create = [
                    Ingredient(name=row[0], measurement_unit=row[1])
                    for row in csv.reader(file)
                ]

            Ingredient.objects.bulk_create(ingredients_to_create)
            print('Импорт данных завершен!')

        except FileNotFoundError:
            print(f'File not found: {file_path}')

        except Exception as error:
            print(f'An error occurred: {error}')
