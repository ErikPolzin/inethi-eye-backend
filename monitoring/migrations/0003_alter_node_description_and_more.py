# Generated by Django 5.0.6 on 2024-06-21 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0002_rename_node_state_uptimemetric_reachable_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='last_contact_from_ip',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]