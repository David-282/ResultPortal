from django.db import models

from core.constants import ROLE_STUDENT, LEVEL_CHOICES
from core.models import User, Department
from util.random_code_generator import matric_code


# Create your models here.


class Student(models.Model):

    STUDENT_STATUS_CHOICES = [
        ("active", "Active"),
        ("suspended", "Suspended"),
        ("graduated", "Graduated"),
        ("withdrawn", "Withdrawn"),

    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile", limit_choices_to={"role": ROLE_STUDENT})
    matric_number = models.CharField(max_length = 20, default = matric_code, unique=True,primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="student_department")
    level = models.CharField(max_length = 20, choices=LEVEL_CHOICES)

    status = models.CharField(max_length= 20, choices = STUDENT_STATUS_CHOICES , default= "active",)
    entry_year = models.PositiveIntegerField()
    enrolled_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    def __str__(self):
        return f"{self.matric_number} - {self.user.get_full_name()}"

    class meta:
        db_table = "student account"
        ordering = ["matric_number"]


    @property
    def full_name(self):
        return self.user.get_full_name()

    @property
    def email(self):
        return self.user.email


    @property
    def is_active(self):
        return self.status


class Staff(models.Model):

    DESIGNATION_CHOICES = [
        ("L1","Lecturer I"),
        ("L2", "Lecturer II"),
        ("SL", "Senior Lecturer"),
        ("Prf", "Professor"),
        ("Hod", "Head of Department")
    ]
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    designation = models.CharField(max_length = 3, choices=DESIGNATION_CHOICES, default="L1")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.user} - {self.designation}"

    class Meta:
        ordering = ['designation']