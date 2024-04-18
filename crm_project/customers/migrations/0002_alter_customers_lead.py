# Generated by Django 5.0.2 on 2024-04-13 12:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customers", "0001_initial"),
        ("leads", "0002_alter_leads_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customers",
            name="lead",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="leads",
                to="leads.leads",
            ),
        ),
    ]