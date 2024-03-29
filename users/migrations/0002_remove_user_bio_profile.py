# Generated by Django 4.2.3 on 2023-07-25 22:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import utils.file_utils


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="bio",
        ),
        migrations.CreateModel(
            name="Profile",
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
                ("bio", models.CharField(default=None, max_length=1024, null=True)),
                (
                    "profile_image",
                    models.ImageField(
                        default=None,
                        null=True,
                        upload_to=utils.file_utils.user_directory_path,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
