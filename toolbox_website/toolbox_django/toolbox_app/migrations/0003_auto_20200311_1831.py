# Generated by Django 3.0.3 on 2020-03-11 17:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox_app', '0002_auto_20200311_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personreviews',
            name='stars',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='toolreviews',
            name='stars',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]