from django.contrib import admin
from .models import Theme, Site, Page, Template, Translation

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'hash', 'created_at')
    search_fields = ('name', 'version', 'hash')
    ordering = ('-created_at',)


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'theme', 'owner', 'created_at')
    search_fields = ('name', 'domain')
    list_filter = ('theme', 'owner')
    ordering = ('-created_at',)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'site', 'status', 'created_by', 'created_at')
    search_fields = ('title', 'slug', 'content')
    list_filter = ('status', 'site', 'created_by')
    ordering = ('-created_at',)


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'rating', 'created_by', 'created_at')
    search_fields = ('name', 'category', 'tags')
    list_filter = ('category',)
    ordering = ('-created_at',)


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ('language_code', 'key', 'value', 'context', 'created_at')
    search_fields = ('language_code', 'key', 'value', 'context')
    list_filter = ('language_code', 'context')
    ordering = ('-created_at',)
