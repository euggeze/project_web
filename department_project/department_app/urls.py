from django.urls import path

from department_app.views import employee_view

urlpatterns = [
    path('employee/', employee_view.employee_list),
]
