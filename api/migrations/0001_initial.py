# Generated by Django 4.2.21 on 2025-05-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ResultEntry",
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
                ("competition", models.CharField(max_length=255)),
                ("room_id", models.CharField(max_length=255)),
                ("command_name", models.CharField(max_length=255)),
                ("user_name", models.CharField(max_length=255)),
                ("scenario", models.CharField(max_length=255)),
                ("flight_time", models.FloatField()),
                ("false_start", models.BooleanField()),
            ],
        ),
    ]
