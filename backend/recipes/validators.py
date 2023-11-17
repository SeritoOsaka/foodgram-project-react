from django.core.validators import RegexValidator

NAME_VALIDATOR_REGEX = r'^[a-zA-Z0-9\s]+$'

name_validator = RegexValidator(
    regex=NAME_VALIDATOR_REGEX,
    message='Название может содержать только буквы, цифры и пробелы.',
    code='invalid_name'
)
color_validator = RegexValidator(
    regex='^#([A-Fa-f0-9]{3,6})$',
    message='Введите цвет в формате HEX.',
    code='invalid_color'
)
