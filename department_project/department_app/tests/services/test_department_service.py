"""Module for testing Department service"""

import requests_mock

from rest_framework.reverse import reverse
from django.test import TestCase


@requests_mock.Mocker()
class DepartmentServiceTestCase(TestCase):
    """Class for testing templates for department view"""

    def test_list_template(self, mocker):
        """Testing list Department template"""
        mocker.get(reverse('department-list'), json=[{'id': 1, 'full_name': 'TEST'},
                                                     {'id': 2, 'full_name': 'TEST'}])
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
        response = self.client.post(
            reverse('departments_create'), data={'id': 1,
                                                 'full_name': 'TEST'})
        self.assertEqual(302, response.status_code)

    def test_delete_template(self, mocker):
        """Testing delete Department template"""
        mocker.get(reverse('department-detail', args=[1]), json={'id': 1,
                                                                 'full_name': 'TEST'})
        mocker.delete(reverse('department-detail', args=[1]))
        response = self.client.post(reverse('departments_delete'), data={'id': 1})
        self.assertEqual(302, response.status_code)

    def test_update_template(self, mocker):
        mocker.get(reverse('department-detail', args=[1]), json={'id': 1,
                                                                 'full_name': 'TEST'})
        mocker.get(reverse('department-list'))
        response = self.client.get(reverse('departments_edit', args=[1]))
        self.assertEqual(200, response.status_code)

    def test_update_finish(self, mocker):
        mocker.get(reverse('department-detail', args=[1]), json={'id': 1,
                                                                 'full_name': 'TEST'})
        mocker.put(reverse('department-detail', args=[1]))
        response = self.client.post(reverse('departments_edit', args=[1]), data={'full_name': 'TEST TEST'})
        self.assertEqual(302, response.status_code)

    def test_create_template_empty(self, mocker):
        """Testing finish create empty Department template"""
        mocker.post(reverse('department-list'))
        response = self.client.post(
            reverse('departments_create'), data={'id': 1, 'full_name': ''})
        self.assertEqual(200, response.status_code)
    
    def test_invalid_update(self,mocker):
        name = 'TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST T'
        mocker.get(reverse('department-detail', args=[1]), json={'id': 1,
                                                                 'full_name': 'TEST'})
        mocker.put(reverse('department-detail', args=[1]))
        response = self.client.post(reverse('departments_edit', args=[1]), data={'full_name': name})
        self.assertEqual(200, response.status_code)
