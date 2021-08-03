"""Module for serialization information"""
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from department_app.models import Department, Employee


class DepartmentSerialize(serializers.ModelSerializer):
    """ Class for serialization Department"""
    average_salary = SerializerMethodField('get_average_salary')

    @staticmethod
    def get_average_salary(obj):
        """Method for counting the average salary of a department
            Keyword argument:
            obj - current object Department

            Return:
            Average salary of the department
        """
        employee_data = Employee.objects.filter(department=obj)
        try:
            return round(sum([x.salary for x in employee_data])/len(employee_data), 2)
        except ZeroDivisionError:
            return 0

    class Meta:
        model = Department
        fields = ['id', 'name', 'average_salary']
