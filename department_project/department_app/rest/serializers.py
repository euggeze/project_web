"""Module for serialization information"""
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from department_app.models import Employee, Department


class EmployeeSerialize(serializers.ModelSerializer):
    """ Class for serialization Employees"""

    class Meta:
        model = Employee
        fields = '__all__'


class DepartmentSerialize(serializers.ModelSerializer):
    """ Class for serialization Department"""
    average_salary = SerializerMethodField('get_average_salary')

    def get_average_salary(self):
        """Function for count average salary"""
        return 1000

    class Meta:
        model = Department
        fields = ['__all__', 'average_salary']
