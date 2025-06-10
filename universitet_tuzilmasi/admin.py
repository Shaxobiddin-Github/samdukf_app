from django.contrib import admin
from .models import Faculty, Chair, Department, Specialty, Group, Semester

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'dean_id', 'created_at')
    search_fields = ('name', 'code')
    list_filter = ('created_at',)
    ordering = ('name',)

@admin.register(Chair)
class ChairAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'faculty', 'head_id', 'created_at')
    search_fields = ('name', 'code')
    list_filter = ('faculty',)
    ordering = ('name',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'head_id', 'created_at')
    search_fields = ('name', 'code')
    ordering = ('name',)

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'faculty', 'created_at')
    search_fields = ('name', 'code')
    list_filter = ('faculty',)
    ordering = ('name',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'education_lang', 'faculty', 'specialty', 'curator_id', 'created_at')
    search_fields = ('name',)
    list_filter = ('education_lang', 'faculty', 'specialty')
    ordering = ('name',)

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'start_date', 'end_date')
    search_fields = ('name', 'code')
    list_filter = ('start_date',)
    ordering = ('start_date',)
