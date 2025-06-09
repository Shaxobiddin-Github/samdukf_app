
from django.db import models
import uuid

class Faculty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=200, db_index=True)
    code = models.CharField(max_length=10, unique=True, db_index=True)
    dean_id = models.UUIDField(null=True, blank=True, db_index=True)  # FK to employees
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return self.name

class Chair(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, db_index=True)
    name = models.CharField(max_length=200, db_index=True)
    code = models.CharField(max_length=10, unique=True, db_index=True)
    head_id = models.UUIDField(null=True, blank=True, db_index=True)  # FK to teachers
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=200, db_index=True)
    code = models.CharField(max_length=10, unique=True, db_index=True)
    head_id = models.UUIDField(null=True, blank=True, db_index=True)  # FK to employees
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return self.name

class Specialty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    code = models.CharField(max_length=10, unique=True, db_index=True)
    name = models.CharField(max_length=200, db_index=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.name

class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=50, unique=True, db_index=True)
    education_lang = models.CharField(max_length=20, db_index=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, db_index=True)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, db_index=True)
    curator_id = models.UUIDField(null=True, blank=True, db_index=True)  # FK to teachers
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.name

class Semester(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    code = models.CharField(max_length=2, unique=True, db_index=True)
    name = models.CharField(max_length=20, db_index=True)
    start_date = models.DateTimeField(db_index=True)
    end_date = models.DateTimeField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.name
