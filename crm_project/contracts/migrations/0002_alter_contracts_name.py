# Generated by Django 5.0.2 on 2024-04-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contracts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contracts",
            name="name",
            field=models.CharField(
                max_length=200, unique=True, verbose_name="Название"
            ),
        ),
    ]
