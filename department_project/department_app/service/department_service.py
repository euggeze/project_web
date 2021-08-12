"""Module for working with departments in site"""
import requests
from django.views.generic import TemplateView
from rest_framework.reverse import reverse


class DepartmentTemplate(TemplateView):
    """ Template for view the list department"""

    def get(self, request, *args, **kwargs):
        """ Function get for list department"""
        department = requests.get('http://127.0.0.1:8000' + reverse('department-list'))
        args = {'data_department': department.json()}
        return self.render_to_response(args)
