from django.contrib import admin
from .models import Student, Employee, Teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'student_id_number', 'first_name', 'second_name', 'gender_code', 'level_code', 'education_year', 'student_status')
    list_filter = ('gender_code', 'level_code', 'education_year', 'student_status')
    search_fields = ('student_id_number', 'first_name', 'second_name', 'short_name')
    ordering = ('-created_at',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'employee_id_number', 'staff_position', 'employment_form', 'employee_status', 'contract_number')
    list_filter = ('employment_form', 'employee_status', 'academic_degree', 'academic_rank')
    search_fields = ('employee_id_number', 'first_name', 'second_name', 'short_name', 'contract_number')
    ordering = ('-created_at',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_id', 'faculty_id', 'chair_id', 'academic_degree', 'academic_rank', 'teaching_experience', 'is_head_of_chair')
    list_filter = ('academic_degree', 'academic_rank', 'is_head_of_chair')
    search_fields = ('employee_id',)
    ordering = ('-created_at',)
