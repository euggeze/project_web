"""Module for testing Employee service"""
import json

import requests_mock

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


@requests_mock.Mocker()
class EmployeeServiceTestCase(APITestCase):
    """Class for testing templates for employee view"""
    adapter = requests_mock.Adapter()

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

    def test_delete_template(self, mocker):
        """Testing delete Employee template"""
        self.adapter.register_uri('GET', reverse('employee-detail', args=[10]), json={'id': 10,
                                                                                      'full_name': 'TEST',
                                                                                      'date_of_birthday': '1999-09-09',
                                                                                      'salary': 1250.50,
                                                                                      'department': 1})
        mocker.delete(reverse('employee-detail', args=[10]))
        response = self.client.get(reverse('employees_delete') + '?id=10')
        self.assertEqual(302, response.status_code)
        self.assertEqual(reverse('employees_list'), response.url)
"""
    def test_update_template(self, mocker):
        self.adapter.register_uri('GET', reverse('employee-detail', args=[10]), json={'id': 10,
                                                                                      'full_name': 'TEST',
                                                                                      'date_of_birthday': '1999-09-09',
                                                                                      'salary': 1250.50,
                                                                                      'department': 1})
        mocker.get(reverse('department-list'))
        mocker.get(reverse('employees_list'))
        mocker.get(reverse('employee-detail', args=[10]))
        response = self.client.get(reverse('employees_edit', args=[10]))
        self.assertEqual(302, response.status_code)
"""