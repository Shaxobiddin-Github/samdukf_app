from django.contrib import admin
from .models import Role, UserRole

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('parent',)
    search_fields = ('name', 'permissions')
    ordering = ('name',)
    readonly_fields = ()

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'role__name')  # Agar User modelda username mavjud bo‘lsa
    ordering = ('user',)
