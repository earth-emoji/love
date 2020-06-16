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
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=128, unique=True)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('funds_needed', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('funds_raised', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('funds_available', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('is_open', models.BooleanField(blank=True, default=True)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('closing_statement', models.TextField(blank=True, null=True)),
                ('volunteers_needed', models.PositiveIntegerField(blank=True, default=0)),
            ],
            options={
                'verbose_name': 'campaign',
                'verbose_name_plural': 'campaigns',
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default=uuid.uuid1, unique=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Blocked', 'Blocked')], max_length=20)),
                ('campaign', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='campaigns.Campaign')),
                ('member', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Member')),
            ],
            options={
                'verbose_name': 'volunteer',
                'verbose_name_plural': 'volunteers',
            },
        ),
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=80, unique=True)),
                ('name', models.CharField(blank=True, max_length=60, unique=True)),
                ('category', models.CharField(blank=True, choices=[('Animals', 'Animals'), ('Environment', 'Environment'), ('Humans', 'Humans')], max_length=15)),
                ('supporters', models.ManyToManyField(blank=True, related_name='causes', to='accounts.Member')),
            ],
            options={
                'verbose_name': 'cause',
                'verbose_name_plural': 'causes',
            },
        ),
        migrations.AddField(
            model_name='campaign',
            name='cause',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaigns', to='campaigns.Cause'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='initiator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaigns', to='accounts.Member'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='volunteers',
            field=models.ManyToManyField(related_name='volunteer_work', through='campaigns.Volunteer', to='accounts.Member'),
        ),
    ]
