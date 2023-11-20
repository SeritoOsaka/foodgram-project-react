import csv

from django.core.management import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        file_path = 'data/ingredients.csv'

        try:
            with open(file_path, encoding='UTF-8') as file:
                reader = csv.DictReader(file)
                ingredients_to_create = [
                    Ingredient(name=row['name'],
                               measurement_unit=row['measurement_unit'])
                    for row in reader
                ]

            Ingredient.objects.bulk_create(ingredients_to_create)
            print('Импорт данных завершен!')

        except FileNotFoundError:
            print(f'File not found: {file_path}')

        except Exception as error:
            print(f'An error occurred: {error}')
