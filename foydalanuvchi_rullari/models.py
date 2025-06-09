
from django.db import models
import uuid

class UserRole(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    user_id = models.UUIDField(db_index=True)  # FK to users.User
    role_id = models.UUIDField(db_index=True)  # FK to roles.Role

    def __str__(self):
        return f"User {self.user_id} - Role {self.role_id}"
