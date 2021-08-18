"""Module for working with employees in site"""
import requests
from django.http import JsonResponse, HttpResponseRedirect

from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from rest_framework.reverse import reverse

from department_app.models import Employee


class EmployeeTemplate(ListView):
    """ Template for view the list employee"""
    model = Employee
    fields = '__all__'
    object_list = None
    
    def get_context_data(self, *, object_list=None, **kwargs):
        """ Function for get data from api"""
        try:
            department = requests.get(reverse('department-list', request=self.request)).json()
        except ValueError:
            department = requests.get(reverse('department-list', request=self.request))
        kwargs.setdefault('data_department', department)
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        return kwargs

    def get(self, request, *args, **kwargs):
        """ Function get for list employee"""
        context = self.get_context_data(**kwargs)
        sel_department = request.GET.get("department", '')
        start = request.GET.get("start", '')
        end = request.GET.get("end", '')
        filter_query = '?department=' + sel_department + '&start=' + start + '&end=' + end
        try:
            employees = requests.get(reverse('employee-list', request=self.request) + filter_query).json()
        except ValueError:
            employees = requests.get(reverse('employee-list', request=self.request) + filter_query)
        if request.is_ajax():
            args = {'data_employee_new': employees}
            return JsonResponse(args)
        context.setdefault('data_employee', employees)
        return self.render_to_response(context)


class EmployeeCreate(CreateView):
    """ Template for view create employee"""
    model = Employee
    fields = '__all__'

    def get_success_url(self):
        """ Function for save page for success completed create"""
        return reverse('employees_list')

    def get_context_data(self, **kwargs):
        """ Function for get data from api"""
        try:
            departments = requests.get(reverse('department-list', request=self.request)).json()
        except ValueError:
            departments = requests.get(reverse('department-list', request=self.request))
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
            print(employee)
            requests.post(reverse('employee-list', request=self.request), data=employee)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class EmployeeEdit(UpdateView):
    """ Template for view edit employee"""
    model = Employee
    fields = '__all__'

    def get_success_url(self):
        """ Function for save page for edit success"""
        return reverse('employees_list')

    def get_context_data(self, **kwargs):
        """ Function for get data from api"""
        try:
            departments = requests.get(reverse('department-list', request=self.request)).json()
        except ValueError:
            departments = requests.get(reverse('department-list', request=self.request))
        try:
            employee = requests.get(
                reverse('employee-detail', request=self.request, args=[self.kwargs['pk']])).json()
        except ValueError:
            employee = requests.get(reverse('department-detail', request=self.request, args=[self.kwargs['pk']]))
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
        else:
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
