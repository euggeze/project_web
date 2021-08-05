"""Module for testing rest-modules"""
from rest_framework.test import APITestCase, APIRequestFactory, APIClient

from department_app.models import Department
from department_app.rest import DepartmentSerialize
from department_app.views import DepartmentViewSet

import json


class DepartmentTestCase(APITestCase):
    """Class for testing CRUD functions
    and unexpected situations for department view"""

    def setUp(self):
        """Added test client"""
        self.factory = APIRequestFactory()
        self.client = APIClient()

    def test_list(self):
        """Testing list departments"""
        response = self.client.get('/api/v1/department/')
        response_data = str(response.json())
        db_data = str(json.dumps(DepartmentSerialize(Department.objects.all(), many=True).data, default=float)).replace(
            '\"', '\'')
        self.assertEqual(200, response.status_code)
        self.assertNotEqual(Department.objects.count(), 0)
        self.assertEqual(response_data, db_data)

    def test_create(self):
        """Testing create a department"""
        past_count = Department.objects.count()
        response = self.client.post('/api/v1/department/', {'name': 'TEST'}, format='json')
        self.assertEqual(201, response.status_code)
        self.assertEqual(past_count + 1, Department.objects.count())
        self.assertTrue(Department.objects.filter(name='TEST').exists())

    def test_update(self):
        """Testing update a department"""
        request = self.factory.put('/api/v1/department/', json.dumps({"name": "TEST"}),
                                   content_type='application/json')
        response = DepartmentViewSet.as_view({'put': 'update'})(request, pk=1)
        self.assertEqual(200, response.status_code)
        self.assertTrue(Department.objects.filter(id=1, name='TEST').exists())

    def test_delete(self):
        """Testing delete a department"""
        request = self.factory.delete('/api/v1/department/')
        response = DepartmentViewSet.as_view({'delete': 'destroy'})(request, pk=1)
        self.assertEqual(204, response.status_code)
        self.assertFalse(Department.objects.filter(id=1).exists())

    def test_create_empty(self):
        """Testing create a empty department"""
        past_count = Department.objects.count()
        response = self.client.post('/api/v1/department/', {'name': ''}, format='json')
        self.assertEqual(400, response.status_code)
        self.assertEqual(past_count, Department.objects.count())
        self.assertFalse(Department.objects.filter(name='').exists())

    def test_create_long(self):
        """Testing create long department name"""
        name = 'TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST T'
        past_count = Department.objects.count()
        response = self.client.post('/api/v1/department/', {'name': name}, format='json')
        self.assertEqual(400, response.status_code)
        self.assertEqual(past_count, Department.objects.count())
        self.assertFalse(Department.objects.filter(name=name).exists())
