# Generated by Django 5.0.4 on 2024-05-01 08:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("purchase_order", "0002_remove_purchaseorder_order_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="purchaseorder",
            name="delivered_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 5, 3, 8, 46, 21, 367705, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AddField(
            model_name="purchaseorder",
            name="issues",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="purchaseorder",
            name="delivery_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 5, 3, 8, 46, 21, 367686, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="purchaseorder",
            name="issue_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 5, 1, 8, 46, 21, 367747, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
