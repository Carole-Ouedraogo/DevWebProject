# Generated by Django 3.0.3 on 2020-05-23 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox_app', '0004_persons_is_authenticated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persons',
            name='is_authenticated',
        ),
    ]
