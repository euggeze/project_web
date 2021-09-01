"""Module for working with departments in site"""
import requests
from django.http import HttpResponseRedirect
from django.views.generic import DeleteView, CreateView, ListView, UpdateView
from django.views.generic.list import MultipleObjectMixin
from rest_framework.reverse import reverse

from department_app.models import Department


class DepartmentTemplate(ListView):
    """ Template for view the list department"""
    model = Department
    fields = '__all__'

    def get_context_data(self, **kwargs):
        """ Function for get data from api"""
        department = requests.get(reverse('department-list', request=self.request)).json()
        data = MultipleObjectMixin.get_context_data(self, **kwargs)
        data['data_department'] = department
        return data


class DepartmentCreate(CreateView):
    """ Template for view create department"""
    model = Department
    fields = '__all__'
    object = None

    def get_success_url(self):
        """ Function for saving page for creation success"""
        return reverse('departments_list')

    def post(self, request, *args, **kwargs):
        """ Function post for create department"""
        form = self.get_form()
        if form.is_valid():
            department = {'full_name': self.request.POST.get('full_name', None)}
            requests.post(reverse('department-list', request=self.request), data=department)
            return HttpResponseRedirect(self.get_success_url())
        return self.form_invalid(form)


class DepartmentEdit(UpdateView):
    """ Template for view save edit department"""
    model = Department
    fields = '__all__'
    object = None

    def get_success_url(self):
        """ Function for save page for edit success"""
        return reverse('departments_list')

    def get_context_data(self, **kwargs):
        """ Function for get data from api"""
        department = requests.get(reverse('department-detail', request=self.request, args=[self.kwargs['pk']])).json()
        data = super().get_context_data(**kwargs)
        data['data_department'] = department
        return data

    def post(self, request, *args, **kwargs):
        """ Function post for edit department"""
        form = self.get_form()
        if form.is_valid():
            department = {'full_name': self.request.POST.get('full_name', None)}
            requests.put(reverse('department-detail', request=self.request, args=[self.kwargs['pk']]), data=department)
            return HttpResponseRedirect(self.get_success_url())
        return self.form_invalid(form)


class DepartmentDelete(DeleteView):
    """ Template for view delete department"""
    model = Department
    fields = ['full_name']

    def get_success_url(self):
        """ Function for save page for delete success"""
        return reverse('departments_list')

    def post(self, request, *args, **kwargs):
        """ Function post for delete department"""
        success_url = self.get_success_url()
        id_department = self.request.POST.get("id", None)
        requests.delete(reverse('department-detail', request=self.request, args=[id_department]))
        return HttpResponseRedirect(success_url)
