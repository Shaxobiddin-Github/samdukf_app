
from django.db import models
import uuid

class UserRole(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    user = models.ForeignKey('asosiy_jadvallar.User', on_delete=models.CASCADE, db_index=True, null=True, blank=True, related_name='foydalanuvchi_rullari_userroles')
    role = models.ForeignKey('asosiy_jadvallar.Role', on_delete=models.CASCADE, db_index=True, null=True, blank=True, related_name='foydalanuvchi_rullari_userroles')

    def __str__(self):
        return f"User {self.user_id} - Role {self.role_id}"
