# Generated by Django 4.1.1 on 2022-10-03 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_remove_user_location_id_user_location"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="location",
        ),
        migrations.AddField(
            model_name="user",
            name="location",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="loc",
                to="users.location",
            ),
        ),
    ]