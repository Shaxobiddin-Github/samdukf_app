
from django.db import models
import uuid

class Theme(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=50, db_index=True)
    data = models.BinaryField()  # ZIP, AES-256
    version = models.CharField(max_length=10, db_index=True)
    hash = models.CharField(max_length=128, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.name} {self.version}"

class Site(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    domain = models.CharField(max_length=100, unique=True, db_index=True)
    settings = models.JSONField(db_index=True)
    theme = models.ForeignKey(Theme, on_delete=models.PROTECT, db_index=True)
    owner = models.ForeignKey('asosiy_jadvallar.User', on_delete=models.CASCADE, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return self.name

class Page(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
        ARCHIVED = 'archived', 'Archived'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, db_index=True)
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    content = models.JSONField(db_index=True)
    status = models.CharField(max_length=10, choices=Status.choices, db_index=True)
    created_by = models.ForeignKey('asosiy_jadvallar.User', on_delete=models.CASCADE, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return self.title

class Template(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    category = models.CharField(max_length=50, db_index=True)
    data = models.JSONField(db_index=True)
    tags = models.JSONField(null=True, blank=True, db_index=True)
    rating = models.FloatField(null=True, blank=True, db_index=True)
    created_by = models.ForeignKey('asosiy_jadvallar.User', on_delete=models.CASCADE, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.name

class Translation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    language_code = models.CharField(max_length=10, db_index=True)
    key = models.CharField(max_length=200, db_index=True)
    value = models.CharField(max_length=1000, db_index=True)
    context = models.CharField(max_length=50, null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return f"{self.language_code}:{self.key}"
