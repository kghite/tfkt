# Generated by Django 4.2.3 on 2023-07-31 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_user_bio_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="tag",
            field=models.CharField(default=None, max_length=16, null=True),
        ),
    ]
