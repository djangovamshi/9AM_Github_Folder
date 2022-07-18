from rest_framework import serializers
from testapp.models import Department,Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields='__all__'

class EmployeeSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class Dept_Name_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['dept_name']