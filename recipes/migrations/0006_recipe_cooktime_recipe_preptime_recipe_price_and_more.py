# Generated by Django 4.2 on 2023-05-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0005_recipe_rating_delete_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="cooktime",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="recipe",
            name="preptime",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="recipe",
            name="price",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="recipe",
            name="servings",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
