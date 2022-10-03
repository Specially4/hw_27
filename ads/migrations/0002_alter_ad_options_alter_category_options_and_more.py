# Generated by Django 4.1.1 on 2022-10-02 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
        ("ads", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ad",
            options={"verbose_name": "Объявление", "verbose_name_plural": "Объявления"},
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Категория", "verbose_name_plural": "Категории"},
        ),
        migrations.RemoveField(
            model_name="ad",
            name="address",
        ),
        migrations.AddField(
            model_name="ad",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ads",
                to="ads.category",
            ),
        ),
        migrations.AddField(
            model_name="ad",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="ad",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ads",
                to="users.user",
            ),
        ),
        migrations.AlterField(
            model_name="ad",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="ad",
            name="price",
            field=models.PositiveIntegerField(),
        ),
    ]