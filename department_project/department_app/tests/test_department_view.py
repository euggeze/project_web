"""Module for testing rest-modules"""
import json

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from department_app.models import Department


class DepartmentTestCase(APITestCase):
    """Class for testing CRUD functions
    and unexpected situations for department view"""

    def test_list(self):
        """Testing list departments"""
        response = self.client.get(reverse('department-list'))
        response_data = response.json()
        db_data = Department.objects.all()
        self.assertEqual(200, response.status_code)
        self.assertNotEqual(Department.objects.count(), 0)
        for i in range(len(db_data)):
            self.assertEqual(response_data[i].get('name'), db_data[i].name)

    def test_get_employee(self):
        """Testing get a department"""
        response = self.client.get(reverse('department-detail', args=[1]))
        response_data = response.json()
        db_data = Department.objects.get(id=1)
        self.assertEqual(200, response.status_code)
        self.assertEqual(response_data.get('name'), db_data.name)

    def test_create(self):
        """Testing create a department"""
        past_count = Department.objects.count()
        response = self.client.post(reverse('department-list'), {'name': 'TEST'}, format='json')
        self.assertEqual(201, response.status_code)
        self.assertEqual(past_count + 1, Department.objects.count())
        self.assertTrue(Department.objects.filter(name='TEST').exists())

    def test_update(self):
        """Testing update a department"""
        response = self.client.put(reverse('department-detail', args=[1]), json.dumps({"name": "TEST"}),
                                   content_type='application/json')
        self.assertEqual(200, response.status_code)
        self.assertTrue(Department.objects.filter(id=1, name='TEST').exists())

    def test_delete(self):
        """Testing delete a department"""
        response = self.client.delete(reverse('department-detail', args=[1]))
        self.assertEqual(204, response.status_code)
        self.assertFalse(Department.objects.filter(id=1).exists())

    def test_create_empty(self):
        """Testing create a empty department"""
        past_count = Department.objects.count()
        response = self.client.post(reverse('department-list'), {'name': ''}, format='json')
        self.assertEqual(400, response.status_code)
        self.assertEqual(past_count, Department.objects.count())
        self.assertFalse(Department.objects.filter(name='').exists())

    def test_create_long(self):
        """Testing create long department name"""
        name = 'TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST T'
        past_count = Department.objects.count()
        response = self.client.post(reverse('department-list'), {'name': name}, format='json')
        self.assertEqual(400, response.status_code)
        self.assertEqual(past_count, Department.objects.count())
        self.assertFalse(Department.objects.filter(name=name).exists())
