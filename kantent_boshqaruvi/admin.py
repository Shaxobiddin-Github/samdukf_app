from django.contrib import admin
from .models import ContentItem, ContentVersion, Comment

@admin.register(ContentItem)
class ContentItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'status', 'created_by', 'created_at', 'updated_at')
    list_filter = ('type', 'status', 'created_at')
    search_fields = ('title', 'metadata')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(ContentVersion)
class ContentVersionAdmin(admin.ModelAdmin):
    list_display = ('content', 'version_number', 'created_by', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content__title',)
    ordering = ('-created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('short_text', 'content', 'parent', 'status', 'created_by', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('text',)
    readonly_fields = ('created_at',)

    def short_text(self, obj):
        return obj.text[:50] + ('...' if len(obj.text) > 50 else '')
    short_text.short_description = 'Text'
