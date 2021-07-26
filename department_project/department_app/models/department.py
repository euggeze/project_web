"""This module for django migration"""
from django.db import models

class Department(models.Model):
    """Class for object structure Department"""
    id_department = models.AutoField(primary_key=True, editable=False)
    name_department = models.CharField(max_length=60,null=False)
