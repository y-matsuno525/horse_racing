# Generated by Django 4.1 on 2024-04-29 08:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("race", "0002_horse"),
    ]

    operations = [
        migrations.AddField(
            model_name="race",
            name="rank",
            field=models.IntegerField(default=0),
        ),
    ]