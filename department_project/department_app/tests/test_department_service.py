"""Module for testing Department service"""

import requests_mock

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


@requests_mock.Mocker()
class DepartmentServiceTestCase(APITestCase):
    """Class for testing templates for department view"""
    adapter = requests_mock.Adapter()

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
            reverse('departments_create') + '?full_name=TEST')
        self.assertEqual(200, response.status_code)

    def test_delete_template(self, mocker):
        """Testing delete Department template"""
        self.adapter.register_uri('GET', reverse('department-detail', args=[10]), json={'id': 10,
                                                                                        'full_name': 'TEST'})
        mocker.delete(reverse('department-detail', args=[10]))
        response = self.client.post(reverse('departments_delete'), data={'id': 10})
        self.assertEqual(302, response.status_code)

"""    def test_update_template(self, mocker):
        self.adapter.register_uri('GET', reverse('department-detail', args=[10]), json={'id': 10,
                                                                                        'full_name': 'TEST'})
        mocker.get(reverse('department-detail', args=[10]))
        response = self.client.get(reverse('departments_edit', args=[10]))
        self.assertEqual(302, response)
"""
