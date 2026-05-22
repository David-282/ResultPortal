from rest_framework import serializers

from academics.models import Course
from core.constants import LEVEL_CHOICES, SEMESTER_CHOICES


class CourseSerializer(serializers.Serializer):

    class Meta:
        model = Course
        fields = ('department','code', 'title', 'credit_units', 'level', 'semester', 'description')