# Generated by Django 4.2.7 on 2023-12-04 00:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_menu", "0004_remove_menu_price_menu_currency_menu_price_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="currency",
            field=models.CharField(
                choices=[
                    ("cp", "cp"),
                    ("sp", "sp"),
                    ("ep", "ep"),
                    ("gp", "gp"),
                    ("pp", "pp"),
                ],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="menu",
            name="description",
            field=models.TextField(
                validators=[
                    django.core.validators.MaxLengthValidator(
                        255, message="Max 255 characters."
                    )
                ]
            ),
        ),
        migrations.AlterField(
            model_name="menu",
            name="item_type",
            field=models.CharField(
                choices=[("dish", "Dish"), ("drink", "Drink")], max_length=10
            ),
        ),
        migrations.AlterField(
            model_name="menu",
            name="name",
            field=models.CharField(
                max_length=255,
                validators=[
                    django.core.validators.MaxLengthValidator(
                        255, message="Max 255 characters."
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="menu",
            name="price_amount",
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(
                        1, message="Must be greater than 0."
                    )
                ]
            ),
        ),
    ]
