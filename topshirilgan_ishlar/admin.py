from django.contrib import admin
from .models import Submission

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'assignment_id', 'student_id', 'submitted_at', 'score')
    list_filter = ('submitted_at',)
    search_fields = ('assignment_id', 'student_id', 'feedback', 'content')
    ordering = ('-submitted_at',)
    readonly_fields = ('file',)
