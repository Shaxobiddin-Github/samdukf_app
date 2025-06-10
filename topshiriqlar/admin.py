from django.contrib import admin
from .models import Assignment

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_id', 'deadline', 'max_score', 'created_at')
    list_filter = ('deadline', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
