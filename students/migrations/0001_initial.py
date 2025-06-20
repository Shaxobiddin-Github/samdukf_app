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
            name="Teacher",
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
                ("employee_id", models.UUIDField(db_index=True)),
                ("faculty_id", models.UUIDField(db_index=True)),
                ("chair_id", models.UUIDField(db_index=True)),
                (
                    "academic_degree",
                    models.CharField(
                        blank=True, db_index=True, max_length=20, null=True
                    ),
                ),
                (
                    "academic_rank",
                    models.CharField(
                        blank=True, db_index=True, max_length=20, null=True
                    ),
                ),
                ("teaching_experience", models.IntegerField(db_index=True)),
                ("subjects", models.JSONField(db_index=True)),
                ("workload", models.FloatField(db_index=True)),
                ("is_head_of_chair", models.BooleanField(db_index=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "updated_at",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
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
                (
                    "employee_id_number",
                    models.CharField(db_index=True, max_length=20, unique=True),
                ),
                ("full_name", models.BinaryField()),
                ("short_name", models.CharField(db_index=True, max_length=50)),
                ("first_name", models.CharField(db_index=True, max_length=50)),
                ("second_name", models.CharField(db_index=True, max_length=50)),
                (
                    "third_name",
                    models.CharField(
                        blank=True, db_index=True, max_length=50, null=True
                    ),
                ),
                ("gender_code", models.CharField(db_index=True, max_length=2)),
                ("birth_date", models.DateTimeField(db_index=True)),
                ("image", models.BinaryField(blank=True, null=True)),
                ("year_of_enter", models.IntegerField(db_index=True)),
                ("faculty_id", models.UUIDField(blank=True, db_index=True, null=True)),
                ("chair_id", models.UUIDField(blank=True, db_index=True, null=True)),
                (
                    "department_id",
                    models.UUIDField(blank=True, db_index=True, null=True),
                ),
                (
                    "academic_degree",
                    models.CharField(
                        blank=True, db_index=True, max_length=20, null=True
                    ),
                ),
                (
                    "academic_rank",
                    models.CharField(
                        blank=True, db_index=True, max_length=20, null=True
                    ),
                ),
                ("employment_form", models.CharField(db_index=True, max_length=20)),
                ("staff_position", models.CharField(db_index=True, max_length=50)),
                ("employee_status", models.CharField(db_index=True, max_length=20)),
                ("contract_number", models.CharField(db_index=True, max_length=20)),
                ("contract_date", models.DateTimeField(db_index=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "updated_at",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                ("hash", models.CharField(db_index=True, max_length=64)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="asosiy_jadvallar.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                (
                    "student_id_number",
                    models.CharField(db_index=True, max_length=20, unique=True),
                ),
                ("full_name", models.BinaryField()),
                ("short_name", models.CharField(db_index=True, max_length=50)),
                ("first_name", models.CharField(db_index=True, max_length=50)),
                ("second_name", models.CharField(db_index=True, max_length=50)),
                (
                    "third_name",
                    models.CharField(
                        blank=True, db_index=True, max_length=50, null=True
                    ),
                ),
                ("gender_code", models.CharField(db_index=True, max_length=2)),
                ("birth_date", models.DateTimeField(db_index=True)),
                ("image", models.BinaryField(blank=True, null=True)),
                ("avg_gpa", models.FloatField(blank=True, db_index=True, null=True)),
                (
                    "total_credit",
                    models.IntegerField(blank=True, db_index=True, null=True),
                ),
                ("faculty_id", models.UUIDField(db_index=True)),
                ("chair_id", models.UUIDField(blank=True, db_index=True, null=True)),
                ("specialty_id", models.UUIDField(db_index=True)),
                ("group_id", models.UUIDField(db_index=True)),
                ("level_code", models.CharField(db_index=True, max_length=2)),
                ("semester_id", models.UUIDField(db_index=True)),
                ("education_year", models.CharField(db_index=True, max_length=9)),
                ("year_of_enter", models.IntegerField(db_index=True)),
                ("student_status", models.CharField(db_index=True, max_length=20)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "updated_at",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="asosiy_jadvallar.user",
                    ),
                ),
            ],
        ),
    ]
