# Generated by Django 5.2 on 2025-04-27 19:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PricingConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(max_length=20)),
                ('distance_limit_km', models.FloatField()),
                ('base_price', models.FloatField()),
                ('additional_price_per_km', models.FloatField()),
                ('waiting_time_free_minutes', models.IntegerField(default=3)),
                ('waiting_charge_per_unit', models.FloatField()),
                ('waiting_charge_unit_minutes', models.IntegerField(default=3)),
                ('multiplier_upto_1hr', models.FloatField(default=1.0)),
                ('multiplier_1_to_2hr', models.FloatField(default=1.25)),
                ('multiplier_2_to_3hr', models.FloatField(default=2.2)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PricingConfigLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=50)),
                ('actor', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricing_app.pricingconfig')),
            ],
        ),
    ]
