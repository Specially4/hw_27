# Generated by Django 4.1.1 on 2022-10-02 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0002_alter_ad_options_alter_category_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ad",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
