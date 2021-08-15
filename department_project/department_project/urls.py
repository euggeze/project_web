"""department_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from department_app import urls
from department_app.service import EmployeeTemplate, EmployeeEdit, EmployeeDelete, EmployeeCreate, \
    DepartmentTemplate, DepartmentEdit, DepartmentDelete, DepartmentCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(urls)),
    path('', EmployeeTemplate.as_view(template_name='list_employee.html'), name='employees_list_start'),
    path('employee/', EmployeeTemplate.as_view(template_name='list_employee.html'), name='employees_list'),
    path('employee/edit/<int:pk>/', EmployeeEdit.as_view(template_name='edit_employee.html'), name='employees_edit'),
    path('employee/delete/', EmployeeDelete.as_view(), name='employees_delete'),
    path('employee/create/', EmployeeCreate.as_view(template_name='create_employee.html'), name='employees_create'),
    path('department/', DepartmentTemplate.as_view(template_name='list_department.html'), name='departments_list'),
    path('department/edit/<int:pk>/', DepartmentEdit.as_view(template_name='edit_department.html'),
         name='departments_edit'),
    path('department/delete/', DepartmentDelete.as_view(), name='departments_delete'),
    path('department/create/', DepartmentCreate.as_view(template_name='create_department.html'),
         name='departments_create'),
]
