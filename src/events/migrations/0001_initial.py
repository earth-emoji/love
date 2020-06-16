# Generated by Django 2.2.12 on 2020-06-16 21:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=80, unique=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('details', models.TextField(blank=True, default='')),
                ('location', models.CharField(blank=True, max_length=200)),
                ('start_time', models.DateTimeField(blank=True)),
                ('end_time', models.DateTimeField(blank=True)),
                ('visibility', models.CharField(blank=True, choices=[('Public', 'Public'), ('Campaign', 'Campaign'), ('Private', 'Private')], max_length=9)),
                ('is_published', models.BooleanField(default=False)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attendees', models.ManyToManyField(blank=True, related_name='events_attended', to='accounts.Member')),
                ('creator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='accounts.Member')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default=uuid.uuid1, unique=True)),
                ('message', models.TextField(blank=True, default='')),
                ('is_attending', models.BooleanField(blank=True, default=False)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attendee', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='accounts.Member')),
                ('event', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='events.Event')),
            ],
            options={
                'verbose_name': 'invitation',
                'verbose_name_plural': 'invitations',
            },
        ),
    ]
