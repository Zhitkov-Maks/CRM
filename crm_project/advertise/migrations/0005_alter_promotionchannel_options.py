# Generated by Django 5.0.2 on 2024-04-19 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("advertise", "0004_promotionchannel_alter_advertise_promotion_channel"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="promotionchannel",
            options={
                "ordering": ("name",),
                "verbose_name": "канал продвижения",
                "verbose_name_plural": "каналы продвижения",
            },
        ),
    ]
