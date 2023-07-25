# Generated by Django 4.2.3 on 2023-07-18 06:50

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Query",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("query", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("active", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ("-created",),
            },
        ),
    ]
