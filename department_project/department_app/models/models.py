"""This module for django migration"""
from django.db import models

class Employee(models.Model):
"Class for object structure Employee"
    id_employee = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=60,null=False)
    date_of_birthday = models.DateField(null=False)
    salary = models.DecimalField(max_digits=9, decimal_places=2,null=False)
    id_department = models.ForeignKey ('Department', on_delete = models.CASCADE, null=False)


class Department(models.Model):
"Class for object structure Department"
    id_department = models.AutoField(primary_key=True, editable=False)
    name_department = models.CharField(max_length=60,null=False)
