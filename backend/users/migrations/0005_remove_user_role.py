# Generated by Django 4.2.6 on 2023-11-16 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_subscribe_check_not_self_subscribe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
