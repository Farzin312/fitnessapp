# Generated by Django 5.0.2 on 2024-03-18 01:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_auto_20240304_1456"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="name",
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]