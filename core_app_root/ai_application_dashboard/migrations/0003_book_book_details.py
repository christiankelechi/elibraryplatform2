# Generated by Django 4.2.6 on 2024-05-18 13:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "core_app_root_ai_application_dashboard",
            "0002_alter_book_cover_alter_book_sample",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="book_details",
            field=models.TextField(blank=True, null=True),
        ),
    ]