"""Module for working with employees in site"""
import requests
from django.http import JsonResponse
from django.shortcuts import redirect

from django.views.generic import TemplateView
from rest_framework.reverse import reverse


class EmployeeTemplate(TemplateView):
    """ Template for view the list employee"""

    def get(self, request, *args, **kwargs):
        """ Function get for list employee"""
        sel_department = request.GET.get("department", None)
        departments = requests.get(reverse('department-list', request=request)).json()
        if sel_department is None or sel_department is '':
            employees = requests.get(reverse('employee-list', request=request)).json()
        else:
            employees = requests.get(reverse('employee-list', request=request) + '?department=' + sel_department).json()
        if request.is_ajax():
            args = {'data_employee_new': employees}
            return JsonResponse(args)
        args = {'data_employee': employees, 'data_department': departments}
        return self.render_to_response(args)


class EmployeeEdit(TemplateView):
    """ Template for view edit employee"""

    def get(self, request, *args, **kwargs):
        """ Function get for edit employee"""
        if self.request.GET.get('full_name', None):
            employee = {'full_name': self.request.GET.get('full_name', None),
                        'date_of_birthday': self.request.GET.get('date_by', None),
                        'salary': self.request.GET.get('salary', None),
                        'department': int(self.request.GET.get('department', None))}
            requests.put(reverse('employee-detail', request=request, args=[self.kwargs['pk']]), data=employee)
            return redirect('employees_list')
        departments = requests.get(reverse('department-list', request=request)).json()
        employee = requests.get(reverse('employee-detail', request=request, args=[self.kwargs['pk']])).json()
        args = {'data_employee': employee, 'data_department': departments}
        return self.render_to_response(args)


class EmployeeDelete(TemplateView):
    """ Template for view delete employee"""

    def get(self, request, *args, **kwargs):
        """ Function get for delete employee"""
        id_employee = self.request.GET.get("id", None)
        requests.delete(reverse('employee-detail', request=request, args=[id_employee]))
        return redirect('employees_list')



