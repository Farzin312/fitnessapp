# Generated by Django 5.0.2 on 2024-03-02 00:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("happiness", "0003_happinessslog_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="HappinesssLog",
            new_name="UserHappinesssLog",
        ),
    ]