"""Module for testing rest-modules"""
from django.test import TestCase, RequestFactory

from department_app.models import Department, Employee
from department_app.views import EmployeeViewSet
import json


class EmployeeTestCase(TestCase):

    def setUp(self):
        """Added test client"""
        self.factory = RequestFactory()
