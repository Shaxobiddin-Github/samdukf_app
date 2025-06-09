
from django.db import models
import uuid

class Assignment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    course_id = models.UUIDField(db_index=True)  # FK to courses.Course
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField(db_index=True)
    deadline = models.DateTimeField(db_index=True)
    max_score = models.FloatField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return self.title
