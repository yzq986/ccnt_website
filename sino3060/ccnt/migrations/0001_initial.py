# Generated by Django 4.2 on 2023-04-25 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="data",
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
                ("file_name_en", models.CharField(max_length=255)),
                ("organization_en", models.CharField(max_length=255)),
                ("country_en", models.CharField(max_length=50)),
                ("province_en", models.CharField(max_length=50)),
                ("municipality_en", models.CharField(max_length=50)),
                ("county_en", models.CharField(max_length=50)),
                ("date_updated", models.DateTimeField()),
                ("link", models.URLField(max_length=255)),
                ("date_published", models.IntegerField()),
                ("month_published", models.IntegerField()),
                ("note", models.TextField()),
                ("file_name", models.CharField(max_length=255)),
                ("organization", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=50)),
                ("province", models.CharField(max_length=50)),
                ("municipality", models.CharField(max_length=50)),
                ("county", models.CharField(max_length=50)),
                ("invalid_link", models.BooleanField(default=False)),
            ],
        ),
    ]