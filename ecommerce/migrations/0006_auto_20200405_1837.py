# Generated by Django 3.0.4 on 2020-04-05 13:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_auto_20200405_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='contact',
            field=models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Mobile No'),
        ),
    ]
