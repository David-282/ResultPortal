from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from account.models import Student
from core.constants import SEMESTER_CHOICES, LEVEL_CHOICES
from core.models import Department


# Create your models here.


class AcademicSession(models.Model):
    name = models.CharField(max_length=20, help_text= "e.g. 2024/2025")
    year = models.PositiveIntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2100)])
    semester = models.CharField(max_length=10,choices= SEMESTER_CHOICES, default="first")
    is_current = models.BooleanField(default = False)
    start_date = models.DateField(null=True,blank=True)
    end_start = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} - {self.get_semester_display()}"

    class Meta:
        db_table = "academic_session"
        ordering = ['year', 'semester']
        unique_together = [("year", "semester")]


class Course(models.Model):

    department = models.ForeignKey(Department, on_delete=models.PROTECT,related_name= "course")
    code = models.CharField(max_length=20, unique=True, blank=False, null=False)
    title = models.CharField(max_length=200)
    credit_unit = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    level = models.CharField(choices=LEVEL_CHOICES, max_length=3, blank = False, default ="100")
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES, default="first")
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "academic_course"
        ordering = ['code']

    def __str__(self):
        return f"{self.code} - ({self.credit_unit} units)"


class CourseRegistration(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name="registrations")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="registrations")
    session = models.ForeignKey(AcademicSession, on_delete=models.PROTECT, related_name="registrations")
    register_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "academics_course_registrations"
        unique_together = [("student","course", "session")]
        ordering = ['session__year', 'course__code']
    # uv run --env-file .env manage.py make migrations
    def __str__(self):
        return f"{self.student} - {self.course.code} ({self.session})"

    def clean(self):
        if self.course__id and self.session__id:
            if self.course.semester != self.session.semester:
                raise ValidationError(
                    f"Course '{self.course.code}' belongs to the "
                    f"{self.course.get_semester_display()} but this session"
                    f"is the {self.session.get_semester_display()}."
                )
