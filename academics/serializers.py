from rest_framework import serializers

from academics.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('department','code', 'title', 'credit_unit', 'level', 'semester', 'description')

    def create(self,validated_data):
        department_id = self.context.get('department_id')
        return Course.objects.create(department_id=department_id, **validated_data)