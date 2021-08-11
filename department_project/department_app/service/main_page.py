import requests
from django.http import JsonResponse

from django.views.generic import TemplateView
from rest_framework.reverse import reverse


class EmployeeTemplate(TemplateView):

    def get(self, request, *args, **kwargs):
        sel_department = request.GET.get("department", None)
        departments = requests.get(reverse('department-list', request=request)).json()
        if sel_department is None or sel_department is '':
            employees = requests.get(reverse('employee-list', request=request)).json()
        else:
            employees = requests.get(reverse('employee-list', request=request)+'?department='+sel_department).json()
        if request.is_ajax():
            args = {'data_employee_new': employees}
            return JsonResponse(args)
        args = {'data_employee': employees, 'data_department': departments}
        return self.render_to_response(args)


class EmployeeEdit(TemplateView):

    def get(self, request, *args, **kwargs):
        employee = requests.put('http://127.0.0.1:8000' + reverse('employee-detail', args=['pk']).json())
        return self.render_to_response(employee)


class DepartmentTemplate(TemplateView):

    def get(self, request, *args, **kwargs):
        department = requests.get('http://127.0.0.1:8000' + reverse('department-list'))
        args = {'data_department': department.json()}
        return self.render_to_response(args)
