"""Module for working with departments in site"""
import requests
from django.shortcuts import redirect
from django.views.generic import TemplateView
from rest_framework.reverse import reverse


class DepartmentTemplate(TemplateView):
    """ Template for view the list department"""

    def get(self, request, *args, **kwargs):
        """ Function get for list department"""
        department = requests.get(reverse('department-list', request=self.request))
        args = {'data_department': department.json()}
        return self.render_to_response(args)


class DepartmentCreate(TemplateView):
    """ Template for view create department"""

    def get(self, request, *args, **kwargs):
        """ Function get for create department"""
        if self.request.GET.get('full_name', None):
            department = {'full_name': self.request.GET.get('full_name', None)}
            requests.post(reverse('department-list', request=self.request), data=department)
            return redirect('departments_list')
        return self.render_to_response({})


class DepartmentEdit(TemplateView):
    """ Template for view edit department"""

    def get(self, request, *args, **kwargs):
        """ Function get for edit department"""
        if self.request.GET.get('full_name', None):
            department = {'full_name': self.request.GET.get('full_name', None)}
            requests.put(reverse('department-detail', request=self.request, args=[self.kwargs['pk']]), data=department)
            return redirect('departments_list')
        department = requests.get(reverse('department-detail', request=self.request, args=[self.kwargs['pk']])).json()
        args = {'data_department': department}
        return self.render_to_response(args)


class DepartmentDelete(TemplateView):
    """ Template for view delete department"""

    def get(self, request, *args, **kwargs):
        """ Function get for delete department"""
        id_department = self.request.GET.get("id", None)
        requests.delete(reverse('department-detail', request=self.request, args=[id_department]))
        return redirect('departments_list')
