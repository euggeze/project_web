"""Module for testing Employee service"""
import requests

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from department_app.models import Employee, Department


class EmployeeServiceTestCase(APITestCase):

    def test_list_service(self):
        response = requests.get('http://testserver'+ reverse('employee-list'))
        self.assertEqual(200, response.request)
        self.assertNotEqual(Employee.objects.count(), 0)
