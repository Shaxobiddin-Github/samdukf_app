
from django.db import models
import uuid

class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=50, db_index=True)
    permissions = models.JSONField(db_index=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, db_index=True)

    def __str__(self):
        return self.name

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    username = models.CharField(max_length=50, unique=True, db_index=True)
    password = models.BinaryField(max_length=128)  # Argon2id hash, 32 bytes salt, but allow for future-proofing
    role = models.ForeignKey(Role, on_delete=models.PROTECT, db_index=True)
    email = models.BinaryField(unique=True, db_index=True)  # AES-256 encrypted
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(null=True, blank=True, db_index=True)
    last_login = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return self.username

class Log(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, db_index=True)
    action = models.CharField(max_length=50, db_index=True)
    object_type = models.CharField(max_length=50, db_index=True)
    object_id = models.UUIDField(db_index=True)
    details = models.JSONField(null=True, blank=True, db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    ip_address = models.CharField(max_length=45, db_index=True)

    def __str__(self):
        return f"{self.action} {self.object_type} by {self.user} at {self.timestamp}"
