from rest_framework import serializers

from academics.models import Course


class CourseSerializer(serializers.Serializer):

    class Meta:
        model = Course
        fields = ('department','code', 'title', 'credit_units', 'level', 'semester', 'description')