from django.contrib import admin

from academics.models import Course


# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','department','credit_unit','code', 'created_at', 'updated_at')
    search_fields = ('title','code','department','credit_unit')