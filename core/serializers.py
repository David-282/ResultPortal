from rest_framework import serializers

from core.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['department_code', 'name', 'description']
    # code = serializers.CharField(max_length=55, required=True)
    # name =  serializers.CharField(max_length=55, required=True)
    # description = serializers.CharField(max_length=255, required=False)


