# Generated by Django 4.2.2 on 2023-06-20 05:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={
                "ordering": ["-publish"],
                "verbose_name": "Запись блога",
                "verbose_name_plural": "Записи блога",
            },
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=250, unique_for_date="publish"),
        ),
    ]
