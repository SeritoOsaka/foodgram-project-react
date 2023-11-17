from django.contrib.auth.models import AbstractUser
from .validators import name_validator, last_name_validator
from django.db import models
from django.contrib.auth.validators import ASCIIUsernameValidator

from .constants import MAX_EMAIL_LENGTH, MAX_NAME_LENGTH, MAX_USERNAME_LENGTH


class User(AbstractUser):
    ADMIN = 'admin'
    name_validator = name_validator
    email = models.EmailField(
        'Адрес эл.почты',
        max_length=MAX_EMAIL_LENGTH,
        unique=True,
    )
    username = models.CharField(
        'Имя пользователя',
        max_length=MAX_USERNAME_LENGTH,
        unique=True,
        validators=[ASCIIUsernameValidator()]
    )
    first_name = models.CharField(
        'Имя',
        max_length=MAX_NAME_LENGTH,
        validators=[name_validator],
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=MAX_NAME_LENGTH,
        validators=[last_name_validator],
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribe',
        verbose_name='Подписчик',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriber',
        verbose_name='Автор',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

        constraints = [
            models.UniqueConstraint(fields=['user', 'author'],
                                    name='unique_subscriber'),
            models.CheckConstraint(check=~models.Q(user=models.F('author')),
                                   name='check_not_self_subscribe'),
        ]
