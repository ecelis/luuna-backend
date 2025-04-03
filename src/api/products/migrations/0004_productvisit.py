# Generated by Django 5.1.7 on 2025-04-03 03:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_alter_brand_managers_alter_product_managers"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductVisit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("visit_timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "ip_address",
                    models.GenericIPAddressField(blank=True, db_index=True, null=True),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="visits",
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
