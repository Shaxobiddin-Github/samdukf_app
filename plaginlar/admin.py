from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'department_id', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    ordering = ('-created_at',)
