# Generated by Django 2.2.12 on 2020-05-20 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20200520_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, max_length=80, unique=True),
        ),
    ]
