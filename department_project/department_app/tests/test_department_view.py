"""Module for testing rest-modules"""
from django.test import TestCase, RequestFactory

from department_app.models import Department
from department_app.views import DepartmentViewSet


class DepartmentTestCase(TestCase):
    """Class for testing CRUD functions
    and unexpected situations for department view"""
    def setUp(self):
        """Added test client"""
        self.factory = RequestFactory()

    def test_list(self):
        """Testing list departments"""
        requests = self.factory.get('/api/v1/department/')
        response = DepartmentViewSet.as_view({'get': 'list'})(requests)
        self.assertEqual(200, response.status_code)
        self.assertNotEqual(Department.objects.count(), 0)

    def test_create(self):
        """Testing create a department"""
        requests = self.factory.post('/api/v1/department/', {'name': 'TEST'}, format='json')
        past_count = Department.objects.count()
        response = DepartmentViewSet.as_view({'post': 'create'})(requests)
        self.assertEqual(201, response.status_code)
        self.assertEqual(past_count + 1, Department.objects.count())
        self.assertTrue(Department.objects.filter(name='TEST').exists())

    def test_update(self):
        """Testing update a department"""
        request = self.factory.put('/api/v1/department/', {'name': 'TEST'},
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
        requests = self.factory.post('/api/v1/department/', {'name': ''}, format='json')
        past_count = Department.objects.count()
        response = DepartmentViewSet.as_view({'post': 'create'})(requests)
        self.assertEqual(400, response.status_code)
        self.assertEqual(past_count, Department.objects.count())
        self.assertFalse(Department.objects.filter(name='').exists())

    def test_create_long(self):
        """Testing create long department name"""
        name = 'TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST T'
        requests = self.factory.post('/api/v1/department/', {'name': name}, format='json')
        past_count = Department.objects.count()
        response = DepartmentViewSet.as_view({'post': 'create'})(requests)
        self.assertEqual(400, response.status_code)
        self.assertEqual(past_count, Department.objects.count())
        self.assertFalse(Department.objects.filter(name=name).exists())
