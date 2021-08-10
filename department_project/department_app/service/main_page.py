import requests
from django.http import JsonResponse, HttpResponse

from django.views.generic import TemplateView
from rest_framework.reverse import reverse


class EmployeeTemplate(TemplateView):

    def get(self, request, *args, **kwargs):
        employees = requests.get('http://127.0.0.1:8000' + reverse('employee-list')).json()
        departments = requests.get('http://127.0.0.1:8000' + reverse('department-list')).json()
        if request.is_ajax:
            selected_dep = request.GET.get("selected_dep", None)
            for x in departments:
                if x.get('name') == str(selected_dep):
                    id_dep = x.get('id')
                    employee = [x for x in employees if x.get('department') == id_dep]
                    print("AAAAAAAA")
                    args = {'data_employee': employee, 'data_department': departments}
                    return HttpResponse(args, 200)
        args = {'data_employee': employees, 'data_department': departments}
        return self.render_to_response(args)


class DepartmentTemplate(TemplateView):

    def get(self, request, *args, **kwargs):
        department = requests.get('http://127.0.0.1:8000' + reverse('department-list'))
        args = {'data_department': department.json()}
        return self.render_to_response(args)
