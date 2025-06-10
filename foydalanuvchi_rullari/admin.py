from django.contrib import admin
from .models import UserRole

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__username', 'role__name')
    list_filter = ('role',)

