"""Module for working with employees in site"""
import requests
from django.http import JsonResponse, HttpResponseRedirect

from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from rest_framework.reverse import reverse

from department_app.models import Employee
from department_app.service.department_service import DepartmentTemplate


class EmployeeTemplate(ListView):
    """ Template for view the list employee"""
    model = Employee
    fields = '__all__'
    object_list = None  # pylint: disable=unused-argument

    def get_context_data(self, *, object_list=None, **kwargs):
        return DepartmentTemplate.get_context_data(self, **kwargs)

    def get(self, request, *args, **kwargs):
        """ Function get for list employee"""
        context = self.get_context_data(**kwargs)
        sel_department = request.GET.get("department", '')
        start = request.GET.get("start", '')
        end = request.GET.get("end", '')
        filter_query = '?department=' + sel_department + '&start=' + start + '&end=' + end
        employees = requests.get(reverse('employee-list', request=self.request) + filter_query).json()
        if request.is_ajax():
            args = {'data_employee_new': employees}
            return JsonResponse(args)
        context.setdefault('data_employee', employees)
        return self.render_to_response(context)


class EmployeeCreate(CreateView):
    """ Template for view create employee"""
    model = Employee
    fields = '__all__'
    object = None

    def get_success_url(self):
        """ Function for save page for success completed create"""
        return reverse('employees_list')

    def get_context_data(self, **kwargs):
        """ Function for get data from api"""
        departments = requests.get(reverse('department-list', request=self.request)).json()
        data = super().get_context_data(**kwargs)
        data['data_department'] = departments
        return data

    def post(self, request, *args, **kwargs):
        """ Function post for create employee"""
        form = self.get_form()
        if form.is_valid():
            employee = {'full_name': self.request.POST.get('full_name', None),
                        'date_of_birthday': self.request.POST.get('date_of_birthday', None),
                        'salary': self.request.POST.get('salary', None),
                        'department': self.request.POST.get('department', None)}
            requests.post(reverse('employee-list', request=self.request), data=employee)
            return HttpResponseRedirect(self.get_success_url())
        return self.form_invalid(form)


class EmployeeEdit(UpdateView):
    """ Template for view edit employee"""
    model = Employee
    fields = '__all__'
    object = None

    def get_success_url(self):
        """ Function for save page for edit success"""
        return reverse('employees_list')

    def get_context_data(self, **kwargs):
        """ Function for get data from api"""
        departments = requests.get(reverse('department-list', request=self.request)).json()
        employee = requests.get(reverse('employee-detail', request=self.request, args=[self.kwargs['pk']])).json()
        data = super().get_context_data(**kwargs)
        data['data_department'] = departments
        data['data_employee'] = employee
        return data

    def post(self, request, *args, **kwargs):
        """ Function post for edit employee"""
        form = self.get_form()
        if form.is_valid():
            employee = {'full_name': self.request.POST.get('full_name', None),
                        'date_of_birthday': self.request.POST.get('date_of_birthday', None),
                        'salary': self.request.POST.get('salary', None),
                        'department': self.request.POST.get('department', None)}
            requests.put(reverse('employee-detail', request=self.request, args=[self.kwargs['pk']]), data=employee)
            return HttpResponseRedirect(self.get_success_url())
        return self.form_invalid(form)


class EmployeeDelete(DeleteView):
    """ Template for view delete employee"""
    model = Employee
    fields = '__all__'

    def get_success_url(self):
        """ Function for save page for delete success"""
        return reverse('employees_list')

    def post(self, request, *args, **kwargs):
        """ Function get for delete department"""
        success_url = self.get_success_url()
        id_employee = self.request.POST.get("id", None)
        requests.delete(reverse('employee-detail', request=self.request, args=[id_employee]))
        return HttpResponseRedirect(success_url)
