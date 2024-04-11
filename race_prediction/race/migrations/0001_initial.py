# Generated by Django 5.0.2 on 2024-04-01 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Race",
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
                ("race_name", models.CharField(max_length=20)),
                ("race_place", models.CharField(max_length=10)),
                ("race_type_and_distance", models.IntegerField(max_length=10)),
                ("race_day_of_the_week", models.CharField(max_length=10)),
                ("race_grade", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Horse",
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
                ("horse_name", models.CharField(max_length=20)),
                ("horse_age", models.IntegerField(max_length=10)),
                ("horse_gender", models.CharField(max_length=10)),
                ("horse_number", models.IntegerField(max_length=10)),
                ("horse_horseman", models.CharField(max_length=20)),
                (
                    "horse_race",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="race.race"
                    ),
                ),
            ],
        ),
    ]