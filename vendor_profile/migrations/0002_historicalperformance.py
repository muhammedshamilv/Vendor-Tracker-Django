# Generated by Django 5.0.4 on 2024-04-27 06:52

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vendor_profile", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalPerformance",
            fields=[
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("on_time_delivery_rate", models.FloatField()),
                ("quality_rating_avg", models.FloatField()),
                ("average_response_time", models.FloatField()),
                ("fulfillment_rate", models.FloatField()),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vendor_profile.vendor",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]