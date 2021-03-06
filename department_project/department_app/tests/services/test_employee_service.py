"""Module for testing Employee service"""

import requests_mock

from rest_framework.reverse import reverse
from django.test import TestCase


@requests_mock.Mocker()
class EmployeeServiceTestCase(TestCase):
    """Class for testing templates for employee view"""

    def test_list_template(self, mocker):
        """Testing list Employee template"""
        checking_data_dep = [{'id': 1, 'full_name': 'TEST'},
                             {'id': 2, 'full_name': 'TEST'}]
        checking_data_emp = [{'id': 1,
                              'full_name': 'TEST',
                              'date_of_birthday': '1999-09-09',
                              'salary': 1250.50,
                              'department': 1}]
        mocker.get(reverse('department-list'), json=checking_data_dep)
        mocker.get(reverse('employee-list'), json=checking_data_emp)
        response = self.client.get(reverse('employees_list'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'list_employee.html')
        self.assertEqual(response.context_data['data_department'], checking_data_dep)
        self.assertEqual(response.context_data['data_employee'], checking_data_emp)

    def test_list_selected(self, mocker):
        """Testing list Employee template"""
        checking_data_dep = [{'id': 1, 'full_name': 'TEST'},
                             {'id': 2, 'full_name': 'TEST'}]
        checking_data_emp = [{'id': 1,
                              'full_name': 'TEST',
                              'date_of_birthday': '1999-09-09',
                              'salary': 1250.50,
                              'department': 1}]
        mocker.get(reverse('department-list'), json=checking_data_dep)
        mocker.get(reverse('employee-list'), json=checking_data_emp)
        response = self.client.get(reverse('employees_list'), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(200, response.status_code)

    def test_create_template(self, mocker):
        """Testing create Employee template"""
        checking_data_dep = [{'id': 1, 'full_name': 'TEST'},
                             {'id': 2, 'full_name': 'TEST'}]
        mocker.get(reverse('department-list'), json=checking_data_dep)
        mocker.post(reverse('employee-list'))
        response = self.client.get(reverse('employees_create'))
        self.assertEqual(200, response.status_code)
        self.assertEqual(checking_data_dep, response.context_data['data_department'])
        self.assertTemplateUsed(response, 'create_employee.html')

    def test_create_template_finish(self, mocker):
        """Testing finish create Employee template"""
        mocker.get(reverse('department-list'), json=[{'id': 1, 'full_name': 'TEST'},
                                                     {'id': 2, 'full_name': 'TEST'}])
        mocker.post(reverse('employee-list'))
        mocker.get(reverse('employees_list'))
        response = self.client.post(
            reverse('employees_create'), data={'id': 1,
                                               'full_name': 'TEST',
                                               'date_of_birthday': '1999-09-09',
                                               'salary': 1250.50,
                                               'department': 1})
        self.assertEqual(302, response.status_code)
        self.assertURLEqual(response.url, '/employee/')

    def test_delete_template(self, mocker):
        mocker.get(reverse('employee-detail', args=[1]), json={'id': 1,
                                                               'full_name': 'TEST',
                                                               'date_of_birthday': '1999-09-09',
                                                               'salary': 1250.50,
                                                               'department': 1})
        mocker.delete(reverse('employee-detail', args=[1]))
        response = self.client.post(reverse('employees_delete'), data={'id': 1})
        self.assertEqual(302, response.status_code)
        self.assertURLEqual(response.url, '/employee/')

    def test_update_template(self, mocker):
        checking_data_dep = [{'id': 1, 'full_name': 'TEST'},
                             {'id': 2, 'full_name': 'TEST'}]
        checking_data_emp = {'id': 1,
                             'full_name': 'TEST',
                             'date_of_birthday': '1999-09-09',
                             'salary': 1250.50,
                             'department': 1}
        mocker.get(reverse('employee-detail', args=[1]), json=checking_data_emp)
        mocker.get(reverse('department-list'), json=checking_data_dep)
        mocker.get(reverse('department-detail', args=[1]))
        response = self.client.get(reverse('employees_edit', args=[1]))
        self.assertEqual(200, response.status_code)
        self.assertEqual(checking_data_dep, response.context_data['data_department'])
        self.assertEqual(checking_data_emp, response.context_data['data_employee'])
        self.assertTemplateUsed(response, 'edit_employee.html')

    def test_update_finish(self, mocker):
        mocker.get(reverse('employee-detail', args=[1]), json={'id': 1,
                                                               'full_name': 'TEST',
                                                               'date_of_birthday': '1999-09-09',
                                                               'salary': 1250.50,
                                                               'department': 1})
        mocker.get(reverse('department-list'), json=[{'id': 1, 'full_name': 'TEST'},
                                                     {'id': 2, 'full_name': 'TEST'}])
        mocker.get(reverse('department-detail', args=[1]))
        mocker.put(reverse('employee-detail', args=[1]))
        response = self.client.post(reverse('employees_edit', args=[1]), data={'full_name': 'TEST TEST',
                                                                               'date_of_birthday': '1999-09-09',
                                                                               'salary': 1251.50,
                                                                               'department': 1})
        self.assertEqual(302, response.status_code)
        self.assertURLEqual(response.url, '/employee/')

    def test_invalid_create(self, mocker):
        mocker.get(reverse('department-list'), json=[{'id': 1, 'full_name': 'TEST'},
                                                     {'id': 2, 'full_name': 'TEST'}])
        mocker.post(reverse('employee-list'))
        mocker.get(reverse('employees_list'))
        response = self.client.post(
            reverse('employees_create'), data={'id': 1,
                                               'full_name': '',
                                               'date_of_birthday': '1999-09-09',
                                               'salary': 1250.50,
                                               'department': 1})
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'create_employee.html')

    def test_invalid_update(self, mocker):
        name = 'TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST T'
        mocker.get(reverse('employee-detail', args=[1]), json={'id': 1,
                                                               'full_name': 'TEST',
                                                               'date_of_birthday': '1999-09-09',
                                                               'salary': 1250.50,
                                                               'department': 1})
        mocker.get(reverse('department-list'), json=[{'id': 1, 'full_name': 'TEST'},
                                                     {'id': 2, 'full_name': 'TEST'}])
        mocker.get(reverse('department-detail', args=[1]))
        mocker.put(reverse('employee-detail', args=[1]))
        response = self.client.post(reverse('employees_edit', args=[1]), data={'full_name': name,
                                                                               'date_of_birthday': '1999-09-09',
                                                                               'salary': 1251.50,
                                                                               'department': 1})
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'edit_employee.html')
