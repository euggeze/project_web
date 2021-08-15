"""Module for testing Employee service"""

import requests_mock

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


@requests_mock.Mocker()
class EmployeeServiceTestCase(APITestCase):
    """Class for testing templates for employee view"""

    def test_list_template(self, mocker):
        """Testing list Employee template"""
        mocker.get(reverse('department-list'))
        mocker.get(reverse('employee-list'))
        response = self.client.get(reverse('employees_list'))
        self.assertEqual(200, response.status_code)

    def test_create_template(self, mocker):
        """Testing create Employee template"""
        mocker.get(reverse('department-list'))
        mocker.post(reverse('employee-list'))
        response = self.client.get(reverse('employees_create'))
        self.assertEqual(200, response.status_code)

    def test_create_template_finish(self, mocker):
        """Testing finish create Employee template"""
        mocker.get(reverse('department-list'))
        mocker.post(reverse('employee-list'))
        mocker.get(reverse('employees_list'))
        response = self.client.get(
            reverse('employees_create') + '?department=1&full_name=Test&date_by=2001-01-01&salary=111')
        self.assertEqual(reverse('employees_list'), response.url)
        self.assertEqual(302, response.status_code)
