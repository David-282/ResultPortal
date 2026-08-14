from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from core.constants import ROLE_CHOICES, ROLE_ADMIN


# Create your models here.
class UserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)

    def create_user(self,email,username,password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email= email, username = username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password= None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", ROLE_ADMIN)
        return self.create_user(email,username,password,**extra_fields)




class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField(max_length = 100, blank=False, null=False, unique=True)
    username = models.CharField(max_length = 100, blank=False, null=False,unique=True)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    role = models.CharField(max_length = 100, choices = ROLE_CHOICES, default = "student")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f"{self.get_full_name()} ({self.username})"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def is_admin(self):
        return self.role == ROLE_ADMIN


class Department(models.Model):
    name = models.CharField(max_length = 100, blank=False, null=False)
    department_code = models.CharField(max_length = 100, blank=False, null=False, unique = True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # department_id = models.CharField(max_length = 100, blank=False, null=False)
    description = models.CharField(max_length = 100, blank=False, null=False)
    is_active = models.BooleanField(default = True)
    updated_at = models.DateTimeField(auto_now = True)


    class Meta:
        db_table = "core_department"
        ordering = ['name']

    def __str__(self):
        return f"{self.department_code}"