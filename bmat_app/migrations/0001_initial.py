# Generated by Django 3.2.4 on 2021-07-05 08:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MusicalWork",
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
                ("title", models.CharField(max_length=60, null=True)),
                (
                    "contributors",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=60), size=None
                    ),
                ),
                ("iswc", models.CharField(max_length=11, null=True, unique=True)),
            ],
        ),
    ]
