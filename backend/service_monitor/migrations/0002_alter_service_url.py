# Generated by Django 5.0 on 2024-03-19 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='url',
            field=models.URLField(max_length=100, unique=True),
        ),
    ]
