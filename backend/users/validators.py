from django.core.validators import RegexValidator

NAME_REGEX = '^[a-zA-Zа-яА-ЯёЁ]+$'
COLOR_REGEX = '^#([A-Fa-f0-9]{3,6})$'

name_validator = RegexValidator(
    regex=NAME_REGEX,
    message='Эти данные могут содержать только буквы и пробелы.'
)
color_validator = RegexValidator(
    regex=COLOR_REGEX,
    message='Введите цвет в формате HEX.',
    code='invalid_color'
)
