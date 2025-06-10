from django.contrib import admin
from .models import ContentItem

@admin.register(ContentItem)
class ContentItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'created_by', 'created_at', 'updated_at')
    list_filter = ('type', 'created_at')
    search_fields = ('title', 'metadata')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
