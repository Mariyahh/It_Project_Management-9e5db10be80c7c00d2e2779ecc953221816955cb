# Generated by Django 4.1.7 on 2023-06-24 10:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0009_remove_recipe_cooktime_remove_recipe_preptime_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="total_preptime",
            field=models.IntegerField(default=0),
        ),
    ]
