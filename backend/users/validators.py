from django.core.validators import RegexValidator

NAME_REGEX = '^[a-zA-Zа-яА-ЯёЁ]+$'
LAST_NAME_REGEX = '^[a-zA-Zа-яА-ЯёЁ]+$'

name_validator = RegexValidator(
    regex=NAME_REGEX,
    message='Имя может содержать только буквы и пробелы.'
)
last_name_validator = RegexValidator(
        regex=LAST_NAME_REGEX,
        message='Фамилия может содержать только буквы и пробелы.'
    )
