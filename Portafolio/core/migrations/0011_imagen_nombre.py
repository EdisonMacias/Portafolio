# Generated by Django 4.2.3 on 2023-09-18 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_alter_portafolio_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="imagen",
            name="nombre",
            field=models.CharField(default=1, max_length=100, verbose_name="Nombre"),
            preserve_default=False,
        ),
    ]
