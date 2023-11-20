import csv

from django.core.management import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Загрузка из csv файла'

    def handle(self, *args, **kwargs):
        file_path = 'data/ingredients.csv'

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                Ingredient.objects.bulk_create(
                    Ingredient(**data) for data in reader)
            self.stdout.write(self.style.SUCCESS('Все ингредиенты загружены'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Файл {file_path} не найден'))
        except Exception as error:
            self.stdout.write(self.style.ERROR(f'Произошла ошибка: {error}'))
