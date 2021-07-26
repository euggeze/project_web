"""This module for django migration"""
from django.db import models


class Department(models.Model):
    """Class for object structure Department"""
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=60, null=False, blank=False)

    class Meta:
        db_table = 'departments'
        verbose_name = 'Department names'
        ordering = ['name']
