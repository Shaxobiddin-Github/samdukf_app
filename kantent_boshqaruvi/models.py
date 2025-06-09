
from django.db import models
import uuid

class ContentItem(models.Model):
    class Type(models.TextChoices):
        ARTICLE = 'article', 'Article'
        MEDIA = 'media', 'Media'
        DOCUMENT = 'document', 'Document'

    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
        ARCHIVED = 'archived', 'Archived'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    type = models.CharField(max_length=20, choices=Type.choices, db_index=True)
    title = models.CharField(max_length=200, db_index=True)
    data = models.BinaryField()  # AES-256
    metadata = models.JSONField(db_index=True)
    status = models.CharField(max_length=10, choices=Status.choices, db_index=True)
    created_by = models.UUIDField(db_index=True)  # FK to users.User
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return f"{self.type}: {self.title}"

class ContentVersion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    content = models.ForeignKey(ContentItem, on_delete=models.CASCADE, db_index=True)
    version_number = models.IntegerField(db_index=True)
    data = models.BinaryField()  # Delta, max 100MB
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    created_by = models.UUIDField(db_index=True)  # FK to users.User

    def __str__(self):
        return f"{self.content.title} v{self.version_number}"

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    content = models.ForeignKey(ContentItem, on_delete=models.CASCADE, db_index=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, db_index=True)
    text = models.TextField(db_index=True)
    media = models.BinaryField(null=True, blank=True)
    status = models.CharField(max_length=50, db_index=True)
    created_by = models.UUIDField(db_index=True)  # FK to users.User
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.text[:30]}..."
