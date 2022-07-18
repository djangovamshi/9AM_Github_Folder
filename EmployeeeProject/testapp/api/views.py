from testapp.models import Department,Employee
from testapp.api.serializers import EmployeeSerilaizer,DepartmentSerializer
from rest_framework import viewsets
import json

class Emplyee_ModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerilaizer


class Department_ModelViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer