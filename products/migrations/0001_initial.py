# Generated by Django 4.2.1 on 2023-06-07 07:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
                ("seq", models.PositiveSmallIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="ProductGroup",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
                ("seq", models.PositiveSmallIntegerField(unique=True)),
                (
                    "category",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="products.productcategory"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(limit_value=0)],
                    ),
                ),
                ("hidden", models.BooleanField(default=False)),
                ("group", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="products.productgroup")),
            ],
        ),
    ]
