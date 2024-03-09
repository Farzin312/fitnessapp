# Generated by Django 5.0.2 on 2024-03-02 03:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("happiness", "0005_alter_userhappinessslog_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userhappinessslog",
            name="happiness_score",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ]
            ),
        ),
    ]
