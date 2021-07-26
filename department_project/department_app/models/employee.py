"""This module for django migration"""
from django.db import models


class Employee(models.Model):
    """Class for object structure Employee"""
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=60, null=False, blank=False)
    date_of_birthday = models.DateField(null=False, blank=False)
    salary = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        db_table = 'employees'
        verbose_name = 'Employee information'
        ordering = ['name']
