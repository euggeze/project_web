"""Module for testing Employee view"""
import json

from rest_framework.test import APITestCase, APIRequestFactory

from department_app.models import Employee


class EmployeeTestCase(APITestCase):
    """Class for testing CRUD functions
    and unexpected situations for employee view"""

    def setUp(self):
        """Added test client"""
        self.factory = APIRequestFactory()

    def test_list(self):
        """Testing list Employee model"""
        response = self.client.get('/api/v1/employee/')
        response_data = response.json()
        db_data = Employee.objects.all()
        self.assertEqual(200, response.status_code)
        self.assertNotEqual(Employee.objects.count(), 0)
        for i in range(len(db_data)):
            self.assertEqual(response_data[i].get('name'), db_data[i].name)
            self.assertEqual(response_data[i].get('date_of_birthday'), str(db_data[i].date_of_birthday))
            self.assertEqual(response_data[i].get('salary'), str(db_data[i].salary))
            self.assertEqual(response_data[i].get('department'), db_data[i].department.id)

    def test_get_employee(self):
        """Testing get a employee"""
        response = self.client.get('/api/v1/employee/1/')
        response_data = response.json()
        db_data = Employee.objects.get(id=1)
        self.assertEqual(200, response.status_code)
        self.assertEqual(response_data.get('name'), db_data.name)
        self.assertEqual(response_data.get('date_of_birthday'), str(db_data.date_of_birthday))
        self.assertEqual(response_data.get('salary'), str(db_data.salary))
        self.assertEqual(response_data.get('department'), db_data.department.id)

    def test_create(self):
        """Testing create a employee"""
        past_count = Employee.objects.filter(department=1).count()
        response = self.client.post('/api/v1/employee/', {'name': 'TEST',
                                                          'date_of_birthday': '1999-09-09',
                                                          'salary': 1250.50,
                                                          'department': 1}, format='json')
        self.assertEqual(201, response.status_code)
        self.assertEqual(past_count + 1, Employee.objects.filter(department=1).count())
        self.assertTrue(Employee.objects.filter(name='TEST').exists())

    def test_update(self):
        """Testing update a employee"""
        response = self.client.put('/api/v1/employee/1/', json.dumps({'name': 'TEST',
                                                                      'date_of_birthday': '1999-09-09',
                                                                      'salary': 1250.50,
                                                                      'department': 1}),
                                   content_type='application/json')
        self.assertEqual(200, response.status_code)
        self.assertTrue(Employee.objects.filter(id=1, name='TEST').exists())

    def test_delete(self):
        """Testing delete a employee"""
        response = self.client.delete('/api/v1/employee/1/')
        self.assertEqual(204, response.status_code)
        self.assertFalse(Employee.objects.filter(id=1).exists())

    def test_delete_department(self):
        """Testing delete a department and checking the employee in department"""
        self.client.post('/api/v1/employee/', {'name': 'TEST',
                                               'date_of_birthday': '1999-09-09',
                                               'salary': 1250.50,
                                               'department': 1}, format='json')
        response = self.client.delete('/api/v1/department/1/')
        self.assertEqual(204, response.status_code)
        self.assertFalse(Employee.objects.filter(name='TEST').exists())

    def test_incorrect_name(self):
        """Testing create a employee" with incorrect name"""
        past_count = Employee.objects.filter(department=1).count()
        response = self.client.post('/api/v1/employee/', {'name': '',
                                                          'date_of_birthday': '1999-09-09',
                                                          'salary': 1250.50,
                                                          'department': 1}, format='json')
        self.assertEqual(400, response.status_code)
        self.assertNotEqual(past_count + 1, Employee.objects.filter(department=1).count())
        self.assertFalse(Employee.objects.filter(name='').exists())

    def test_incorrect_date(self):
        """Testing create a employee with incorrect date"""
        past_count = Employee.objects.filter(department=1).count()
        response = self.client.post('/api/v1/employee/', {'name': 'TEST',
                                                          'date_of_birthday': '1999.09.09',
                                                          'salary': 1250.50,
                                                          'department': 1}, format='json')
        self.assertEqual(400, response.status_code)
        self.assertNotEqual(past_count + 1, Employee.objects.filter(department=1).count())
        self.assertFalse(Employee.objects.filter(name='').exists())

    def test_incorrect_salary(self):
        """Testing create a employee with incorrect salary"""
        past_count = Employee.objects.filter(department=1).count()
        response = self.client.post('/api/v1/employee/', {'name': 'TEST',
                                                          'date_of_birthday': '1999-09-09',
                                                          'salary': '1250,50',
                                                          'department': 1}, format='json')
        self.assertEqual(400, response.status_code)
        self.assertNotEqual(past_count + 1, Employee.objects.filter(department=1).count())
        self.assertFalse(Employee.objects.filter(name='').exists())
