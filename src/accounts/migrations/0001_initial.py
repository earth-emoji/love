# Generated by Django 2.2.12 on 2020-06-16 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=80, unique=True)),
            ],
            options={
                'verbose_name': 'member',
                'verbose_name_plural': 'members',
            },
        ),
    ]
