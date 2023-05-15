# Generated by Django 3.2.18 on 2023-05-15 20:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastfood', '0004_alter_booking_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone_number',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+99-999999999'. Up to 14 digits allowed.", regex='^\\+?\\d{1,3}[-\\.\\s]?\\d{1,14}[-\\.\\s]?\\d{1,14}$')]),
        ),
    ]
