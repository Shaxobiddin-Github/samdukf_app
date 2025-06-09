
from django.db import models
import uuid

class Submission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    assignment_id = models.UUIDField(db_index=True)  # FK to assignments.Assignment
    student_id = models.UUIDField(db_index=True)  # FK to students.Student
    content = models.TextField(null=True, blank=True, db_index=True)
    file = models.BinaryField(null=True, blank=True)
    submitted_at = models.DateTimeField(db_index=True)
    score = models.FloatField(null=True, blank=True, db_index=True)
    feedback = models.TextField(null=True, blank=True, db_index=True)

    def __str__(self):
        return f"Submission {self.id}"
