# Generated by Django 2.2.12 on 2020-05-20 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200517_0716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='description',
            new_name='details',
        ),
        migrations.RenameField(
            model_name='invitation',
            old_name='accepted',
            new_name='is_attending',
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
