# Generated by Django 5.0.2 on 2024-04-22 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("advertise", "0003_alter_advertise_promotion_channel"),
    ]

    operations = [
        migrations.CreateModel(
            name="PromotionChannel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=200, unique=True, verbose_name="Канал продвижения"
                    ),
                ),
            ],
            options={
                "verbose_name": "канал продвижения",
                "verbose_name_plural": "каналы продвижения",
                "ordering": ("name",),
            },
        ),
        migrations.AlterField(
            model_name="advertise",
            name="promotion_channel",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="advertise.promotionchannel",
                verbose_name="Канал продвижения",
            ),
        ),
    ]
