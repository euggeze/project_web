"""Module for working with Department model"""
from rest_framework.viewsets import ModelViewSet

from department_app.models import Department
from department_app.rest import DepartmentSerialize


class DepartmentViewSet(ModelViewSet):
    """Class for selecting queryset and
        serializer_class"""
    serializer_class = DepartmentSerialize
    queryset = Department.objects.all()
