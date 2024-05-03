# Generated by Django 5.0.4 on 2024-05-03 03:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("purchase_order", "0004_alter_purchaseorder_delivered_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchaseorder",
            name="delivery_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 5, 5, 3, 42, 2, 50197, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="purchaseorder",
            name="issue_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 5, 3, 3, 42, 2, 50274, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="purchaseorder",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Completed", "Completed"),
                    ("Canceled", "Canceled"),
                ],
                default="Pending",
                max_length=100,
            ),
        ),
    ]