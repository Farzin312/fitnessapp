# Generated by Django 5.0.2 on 2024-03-07 03:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("diet", "0005_alter_userdietlog_options_alter_userfooditem_options"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="userfooditem",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="userdietlog",
            name="daily_satisfaction",
            field=models.IntegerField(
                default=0,
                help_text="Overall daily satisfaction level on a scale of 1-10",
            ),
        ),
        migrations.AddField(
            model_name="userdietlogentry",
            name="satisfaction_level",
            field=models.IntegerField(
                default=0, help_text="Satisfaction level on a scale of 1-10"
            ),
        ),
        migrations.AddField(
            model_name="userfooditem",
            name="is_user_added",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="userfooditem",
            name="serving_size",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Serving size in grams",
                max_digits=5,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="userfooditem",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
