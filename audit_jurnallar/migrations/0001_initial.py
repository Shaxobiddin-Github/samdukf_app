# Generated by Django 5.2.2 on 2025-06-10 05:50

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("asosiy_jadvallar", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AuditLog",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("action", models.CharField(db_index=True, max_length=100)),
                ("timestamp", models.DateTimeField(db_index=True)),
                ("details", models.JSONField(blank=True, db_index=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="asosiy_jadvallar.user",
                    ),
                ),
            ],
        ),
    ]
