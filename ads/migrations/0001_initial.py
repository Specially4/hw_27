# Generated by Django 4.1.1 on 2022-09-24 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ad",
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
                ("name", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=50)),
                ("price", models.IntegerField()),
                ("description", models.TextField()),
                ("address", models.CharField(max_length=100)),
                (
                    "is_published",
                    models.BooleanField(
                        choices=[(True, "Опубликовано"), (False, "Не опубликовано")],
                        default=False,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
    ]
