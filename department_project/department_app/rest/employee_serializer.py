"""Module for serialization information"""
from rest_framework import serializers

from department_app.models import Employee


class EmployeeSerialize(serializers.ModelSerializer):
    """ Class for serialization Employees"""

    class Meta:
        model = Employee
        fields = '__all__'


