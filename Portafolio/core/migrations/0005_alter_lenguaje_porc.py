# Generated by Django 4.2.3 on 2023-09-17 18:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_lenguaje"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lenguaje",
            name="porc",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(
                        0, message="El valor no puede ser menor que 0."
                    ),
                    django.core.validators.MaxValueValidator(
                        100, message="El valor no puede ser mayor que 100."
                    ),
                ],
                verbose_name="Porcentaje",
            ),
        ),
    ]
