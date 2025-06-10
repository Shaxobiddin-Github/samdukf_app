
from django.db import models
import uuid

class AuditLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    user = models.ForeignKey('asosiy_jadvallar.User', on_delete=models.CASCADE, db_index=True, null=True, blank=True)
    action = models.CharField(max_length=100, db_index=True)
    timestamp = models.DateTimeField(db_index=True)
    details = models.JSONField(null=True, blank=True, db_index=True)

    def __str__(self):
        return f"{self.user_id} - {self.action} at {self.timestamp}"
