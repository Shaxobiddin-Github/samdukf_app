
from django.db import models
import uuid

class AuditLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    user_id = models.UUIDField(db_index=True)  # FK to users.User
    action = models.CharField(max_length=100, db_index=True)
    timestamp = models.DateTimeField(db_index=True)
    details = models.JSONField(null=True, blank=True, db_index=True)

    def __str__(self):
        return f"{self.user_id} - {self.action} at {self.timestamp}"
