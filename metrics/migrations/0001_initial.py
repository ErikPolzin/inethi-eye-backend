# Generated by Django 5.0.6 on 2024-06-30 10:27

import django.db.models.deletion
import macaddress.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('mac', macaddress.fields.MACAddressField(integer=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='DataUsageMetric',
            fields=[
                ('metric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='metrics.metric')),
                ('tx_bytes', models.BigIntegerField()),
                ('rx_bytes', models.BigIntegerField()),
            ],
            bases=('metrics.metric',),
        ),
        migrations.CreateModel(
            name='FailuresMetric',
            fields=[
                ('metric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='metrics.metric')),
                ('tx_packets', models.BigIntegerField()),
                ('rx_packets', models.BigIntegerField()),
                ('tx_dropped', models.IntegerField(blank=True, null=True)),
                ('rx_dropped', models.IntegerField(blank=True, null=True)),
                ('tx_retries', models.IntegerField(blank=True, null=True)),
                ('tx_errors', models.IntegerField(blank=True, null=True)),
                ('rx_errors', models.IntegerField(blank=True, null=True)),
            ],
            bases=('metrics.metric',),
        ),
        migrations.CreateModel(
            name='ResourcesMetric',
            fields=[
                ('metric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='metrics.metric')),
                ('memory', models.FloatField()),
                ('cpu', models.FloatField(blank=True, null=True)),
            ],
            bases=('metrics.metric',),
        ),
        migrations.CreateModel(
            name='RTTMetric',
            fields=[
                ('metric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='metrics.metric')),
                ('rtt_min', models.FloatField(blank=True, null=True)),
                ('rtt_avg', models.FloatField(blank=True, null=True)),
                ('rtt_max', models.FloatField(blank=True, null=True)),
            ],
            bases=('metrics.metric',),
        ),
        migrations.CreateModel(
            name='UptimeMetric',
            fields=[
                ('metric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='metrics.metric')),
                ('reachable', models.BooleanField()),
                ('loss', models.IntegerField()),
            ],
            bases=('metrics.metric',),
        ),
    ]
