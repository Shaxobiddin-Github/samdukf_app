
from django.db import models
import uuid

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    user = models.ForeignKey('asosiy_jadvallar.User', on_delete=models.CASCADE, db_index=True)
    student_id_number = models.CharField(max_length=20, unique=True, db_index=True)
    full_name = models.BinaryField()  # AES-256
    short_name = models.CharField(max_length=50, db_index=True)
    first_name = models.CharField(max_length=50, db_index=True)
    second_name = models.CharField(max_length=50, db_index=True)
    third_name = models.CharField(max_length=50, null=True, blank=True, db_index=True)
    gender_code = models.CharField(max_length=2, db_index=True)
    birth_date = models.DateTimeField(db_index=True)
    image = models.BinaryField(null=True, blank=True)
    avg_gpa = models.FloatField(null=True, blank=True, db_index=True)
    total_credit = models.IntegerField(null=True, blank=True, db_index=True)
    faculty_id = models.UUIDField(db_index=True)  # FK to faculties.Faculty
    chair_id = models.UUIDField(null=True, blank=True, db_index=True)  # FK to chairs.Chair
    specialty_id = models.UUIDField(db_index=True)  # FK to specialties.Specialty
    group_id = models.UUIDField(db_index=True)  # FK to groups.Group
    level_code = models.CharField(max_length=2, db_index=True)
    semester_id = models.UUIDField(db_index=True)  # FK to semesters.Semester
    education_year = models.CharField(max_length=9, db_index=True)
    year_of_enter = models.IntegerField(db_index=True)
    student_status = models.CharField(max_length=20, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return self.short_name

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    user = models.ForeignKey('asosiy_jadvallar.User', on_delete=models.CASCADE, db_index=True)
    employee_id_number = models.CharField(max_length=20, unique=True, db_index=True)
    full_name = models.BinaryField()  # AES-256
    short_name = models.CharField(max_length=50, db_index=True)
    first_name = models.CharField(max_length=50, db_index=True)
    second_name = models.CharField(max_length=50, db_index=True)
    third_name = models.CharField(max_length=50, null=True, blank=True, db_index=True)
    gender_code = models.CharField(max_length=2, db_index=True)
    birth_date = models.DateTimeField(db_index=True)
    image = models.BinaryField(null=True, blank=True)
    year_of_enter = models.IntegerField(db_index=True)
    faculty_id = models.UUIDField(null=True, blank=True, db_index=True)  # FK to faculties.Faculty
    chair_id = models.UUIDField(null=True, blank=True, db_index=True)  # FK to chairs.Chair
    department_id = models.UUIDField(null=True, blank=True, db_index=True)  # FK to departments.Department
    academic_degree = models.CharField(max_length=20, null=True, blank=True, db_index=True)
    academic_rank = models.CharField(max_length=20, null=True, blank=True, db_index=True)
    employment_form = models.CharField(max_length=20, db_index=True)
    staff_position = models.CharField(max_length=50, db_index=True)
    employee_status = models.CharField(max_length=20, db_index=True)
    contract_number = models.CharField(max_length=20, db_index=True)
    contract_date = models.DateTimeField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(null=True, blank=True, db_index=True)
    hash = models.CharField(max_length=64, db_index=True)

    def __str__(self):
        return self.short_name

class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    employee_id = models.UUIDField(db_index=True)  # FK to employees.Employee
    faculty_id = models.UUIDField(db_index=True)  # FK to faculties.Faculty
    chair_id = models.UUIDField(db_index=True)  # FK to chairs.Chair
    academic_degree = models.CharField(max_length=20, null=True, blank=True, db_index=True)
    academic_rank = models.CharField(max_length=20, null=True, blank=True, db_index=True)
    teaching_experience = models.IntegerField(db_index=True)
    subjects = models.JSONField(db_index=True)
    workload = models.FloatField(db_index=True)
    is_head_of_chair = models.BooleanField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return str(self.id)
