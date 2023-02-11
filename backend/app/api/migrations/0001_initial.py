# Generated by Django 4.1.3 on 2022-12-18 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField()),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                ("is_superuser", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=False)),
                ("is_email_verified", models.BooleanField(default=False)),
                ("username", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=250)),
            ],
        ),
    ]