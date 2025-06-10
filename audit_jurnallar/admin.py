from django.contrib import admin
from .models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
    search_fields = ('action', 'user__username')
    list_filter = ('action', 'timestamp')
    ordering = ('-timestamp',)
    readonly_fields = ('user', 'action', 'timestamp', 'details')
