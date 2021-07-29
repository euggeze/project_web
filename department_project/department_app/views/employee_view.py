from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from department_app import models
from department_app.rest.serializers import EmployeeSerialize


def employee_list():
    serializer = EmployeeSerialize()
    print(repr(serializer))
