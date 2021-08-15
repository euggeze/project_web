"""Module for testing Department service"""

import requests_mock

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


@requests_mock.Mocker()
class DepartmentServiceTestCase(APITestCase):
    """Class for testing templates for department view"""

    def test_list_template(self, mocker):
        """Testing list Department template"""
        mocker.get(reverse('department-list'))
        response = self.client.get(reverse('departments_list'))
        self.assertEqual(200, response.status_code)

    def test_create_template(self, mocker):
        """Testing create Department template"""
        mocker.post(reverse('department-list'))
        response = self.client.get(reverse('departments_create'))
        self.assertEqual(200, response.status_code)

    def test_create_template_finish(self, mocker):
        """Testing finish create Department template"""
        mocker.post(reverse('department-list'))
        response = self.client.get(
            reverse('departments_create') + '?department=Testing')
        self.assertEqual(reverse('departments_list'), response.url)
        self.assertEqual(302, response.status_code)
