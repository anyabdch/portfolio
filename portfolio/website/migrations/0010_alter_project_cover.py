# Generated by Django 4.2.14 on 2024-09-07 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0009_alter_project_cover"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="cover",
            field=models.FilePathField(path="./static/website/images"),
        ),
    ]
