# Generated by Django 5.0 on 2024-06-21 14:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
