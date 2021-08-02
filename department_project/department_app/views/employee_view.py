"""Module for working with Employee model"""
from rest_framework.viewsets import ModelViewSet

from department_app.models import Employee
from department_app.rest import EmployeeSerialize


class EmployeeViewSet(ModelViewSet):
    """Class for selecting queryset and
    serializer_class"""
    serializer_class = EmployeeSerialize
    queryset = Employee.objects.all()
