# Generated by Django 5.0.2 on 2024-03-02 02:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("happiness", "0004_rename_happinessslog_userhappinessslog"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userhappinessslog",
            options={"ordering": ["-date"]},
        ),
    ]
