# Generated by Django 3.0.3 on 2020-03-08 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox_app', '0002_remove_persons_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='persons',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]