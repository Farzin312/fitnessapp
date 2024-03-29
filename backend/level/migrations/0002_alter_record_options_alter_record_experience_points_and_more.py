# Generated by Django 5.0.2 on 2024-03-02 02:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("level", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="record",
            options={"ordering": ["-date"]},
        ),
        migrations.AlterField(
            model_name="record",
            name="experience_points",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="userlevel",
            name="experience_points",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="userlevel",
            name="level",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
