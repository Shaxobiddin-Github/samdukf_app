from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'hemis_id', 'full_name', 'created_at')
    search_fields = ('student_id', 'hemis_id', 'full_name')
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'updated_at')

