# Generated by Django 5.0.4 on 2024-04-27 07:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vendor_profile", "0002_historicalperformance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vendor",
            name="average_response_time",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="fulfillment_rate",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="on_time_delivery_rate",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="quality_rating_avg",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
