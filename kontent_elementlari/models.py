
from django.db import models
import uuid

class ContentItem(models.Model):
    class Type(models.TextChoices):
        ARTICLE = 'article', 'Article'
        VIDEO = 'video', 'Video'
        DOCUMENT = 'document', 'Document'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    type = models.CharField(max_length=20, choices=Type.choices, db_index=True)
    title = models.CharField(max_length=255, db_index=True)
    data = models.BinaryField()  # AES-256
    metadata = models.JSONField(db_index=True)
    created_by = models.UUIDField(db_index=True)  # FK to users.User
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return self.title
