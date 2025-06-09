
from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    student_id = models.CharField(max_length=50, unique=True, db_index=True)
    hemis_id = models.CharField(max_length=50, unique=True, null=True, blank=True, db_index=True)
    full_name = models.CharField(max_length=200, db_index=True)
    password_hash = models.CharField(max_length=255)
    created_by = models.UUIDField(db_index=True)  # FK to users.User
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return self.full_name
