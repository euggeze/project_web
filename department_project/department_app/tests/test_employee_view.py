"""Module for testing rest-modules"""
from django.test import TestCase, RequestFactory

from department_app.models import Employee
from department_app.views import EmployeeViewSet, DepartmentViewSet


class EmployeeTestCase(TestCase):
    """Class for testing CRUD functions
    and unexpected situations for employee view"""

    def setUp(self):
        """Added test client"""
        self.factory = RequestFactory()

    def test_list(self):
        """Testing list Employee model"""
        requests = self.factory.get('/api/v1/employee/')
        response = EmployeeViewSet.as_view({'get': 'list'})(requests)
        self.assertEqual(200, response.status_code)
        self.assertNotEqual(Employee.objects.count(), 0)

    def test_create(self):
        """Testing create a employee"""
        requests = self.factory.post('/api/v1/employee/', {'name': 'TEST',
                                                           'date_of_birthday': '1999-09-09',
                                                           'salary': 1250.50,
                                                           'department': 1}, format='json')
        past_count = Employee.objects.filter(department=1).count()
        response = EmployeeViewSet.as_view({'post': 'create'})(requests)
        self.assertEqual(201, response.status_code)
        self.assertEqual(past_count + 1, Employee.objects.filter(department=1).count())
        self.assertTrue(Employee.objects.filter(name='TEST').exists())

    def test_update(self):
        """Testing update a employee"""
        request = self.factory.put('/api/v1/employee/', {'name': 'TEST',
                                                         'date_of_birthday': '1999-09-09',
                                                         'salary': 1250.50,
                                                         'department': 1},
                                   content_type='application/json')
        response = EmployeeViewSet.as_view({'put': 'update'})(request, pk=1)
        self.assertEqual(200, response.status_code)
        self.assertTrue(Employee.objects.filter(id=1, name='TEST').exists())

    def test_delete(self):
        """Testing delete a employee"""
        request = self.factory.delete('/api/v1/employee/')
        response = EmployeeViewSet.as_view({'delete': 'destroy'})(request, pk=1)
        self.assertEqual(204, response.status_code)
        self.assertFalse(Employee.objects.filter(id=1).exists())

    def test_delete_department(self):
        """Testing delete a department and checking the employee in department"""
        request_create = self.factory.post('/api/v1/employee/', {'name': 'TEST',
                                                                 'date_of_birthday': '1999-09-09',
                                                                 'salary': 1250.50,
                                                                 'department': 1}, format='json')
        response_create = EmployeeViewSet.as_view({'post': 'create'})(request_create)
        request = self.factory.delete('/api/v1/department/')
        response = DepartmentViewSet.as_view({'delete': 'destroy'})(request, pk=1)
        self.assertEqual(204, response.status_code)
        self.assertFalse(Employee.objects.filter(name='TEST').exists())

    def test_incorrect_name(self):
        """Testing create a employee" with incorrect name"""
        requests = self.factory.post('/api/v1/employee/', {'name': '',
                                                           'date_of_birthday': '1999-09-09',
                                                           'salary': 1250.50,
                                                           'department': 1}, format='json')
        past_count = Employee.objects.filter(department=1).count()
        response = EmployeeViewSet.as_view({'post': 'create'})(requests)
        self.assertEqual(400, response.status_code)
        self.assertNotEqual(past_count + 1, Employee.objects.filter(department=1).count())
        self.assertFalse(Employee.objects.filter(name='').exists())

    def test_incorrect_date(self):
        """Testing create a employee with incorrect date"""
        requests = self.factory.post('/api/v1/employee/', {'name': 'TEST',
                                                           'date_of_birthday': '1999.09.09',
                                                           'salary': 1250.50,
                                                           'department': 1}, format='json')
        past_count = Employee.objects.filter(department=1).count()
        response = EmployeeViewSet.as_view({'post': 'create'})(requests)
        self.assertEqual(400, response.status_code)
        self.assertNotEqual(past_count + 1, Employee.objects.filter(department=1).count())
        self.assertFalse(Employee.objects.filter(name='').exists())

    def test_incorrect_salary(self):
        """Testing create a employee with incorrect salary"""
        requests = self.factory.post('/api/v1/employee/', {'name': 'TEST',
                                                           'date_of_birthday': '1999-09-09',
                                                           'salary': '1250,50',
                                                           'department': 1}, format='json')
        past_count = Employee.objects.filter(department=1).count()
        response = EmployeeViewSet.as_view({'post': 'create'})(requests)
        self.assertEqual(400, response.status_code)
        self.assertNotEqual(past_count + 1, Employee.objects.filter(department=1).count())
        self.assertFalse(Employee.objects.filter(name='').exists())
