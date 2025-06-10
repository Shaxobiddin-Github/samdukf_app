from django.contrib import admin
from .models import Role, User, Log

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)
    list_filter = ('parent',)
    ordering = ('name',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'created_at', 'last_login')
    search_fields = ('username',)
    list_filter = ('role',)
    ordering = ('username', 'created_at')
    readonly_fields = ('created_at', 'updated_at', 'last_login')

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'object_type', 'object_id', 'timestamp', 'ip_address')
    search_fields = ('action', 'object_type', 'ip_address')
    list_filter = ('action', 'object_type', 'timestamp')
    ordering = ('-timestamp',)
