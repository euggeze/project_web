"""Module for testing rest-modules"""
from django.test import TestCase, RequestFactory

from department_app.models import Department
from department_app.views import EmployeeViewSet, DepartmentViewSet
from department_app.rest import DepartmentSerialize


class AverageSalaryTestCase(TestCase):
    """Class for testing CRUD functions
    and unexpected situations for employee view"""

    def setUp(self):
        """Added test client"""
        self.factory = RequestFactory()

    def test_count(self):
        """Testing count average salary in the department"""
        requests_department = self.factory.post('/api/v1/department/', {'name': 'TEST'}, format='json')
        DepartmentViewSet.as_view({'post': 'create'})(requests_department)
        id_department = Department.objects.get(name='TEST').id
        requests_employee1 = self.factory.post('/api/v1/employee/', {'name': 'TEST',
                                                                     'date_of_birthday': '1999-09-09',
                                                                     'salary': 1250.50,
                                                                     'department': id_department}, format='json')
        EmployeeViewSet.as_view({'post': 'create'})(requests_employee1)
        requests_employee2 = self.factory.post('/api/v1/employee/', {'name': 'TEST TEST',
                                                                     'date_of_birthday': '1999-10-09',
                                                                     'salary': 968.00,
                                                                     'department': id_department}, format='json')
        EmployeeViewSet.as_view({'post': 'create'})(requests_employee2)
        test = DepartmentSerialize.get_average_salary(Department.objects.get(name='TEST'))
        self.assertEqual(1109.25, test)

    def test_count_empty(self):
        """Testing count average salary if the department is empty"""
        requests_department = self.factory.post('/api/v1/department/', {'name': 'TEST'}, format='json')
        DepartmentViewSet.as_view({'post': 'create'})(requests_department)
        test = DepartmentSerialize.get_average_salary(Department.objects.get(name='TEST'))
        self.assertEqual(0, test)
