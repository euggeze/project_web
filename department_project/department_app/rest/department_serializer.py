"""Module for serialization information"""
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from department_app.models import Department


class DepartmentSerialize(serializers.ModelSerializer):
    """ Class for serialization Department"""
    average_salary = SerializerMethodField('get_average_salary')

    @staticmethod
    def get_average_salary(plug):
        """Function for count average salary"""
        return 1000

    class Meta:
        model = Department
        fields = ['id', 'name', 'average_salary']
