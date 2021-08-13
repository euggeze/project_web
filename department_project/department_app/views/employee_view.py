"""Module for working with Employee model"""
from rest_framework.viewsets import ModelViewSet

from department_app.models import Employee, Department
from department_app.rest import EmployeeSerialize


class EmployeeViewSet(ModelViewSet):
    """Class for selecting queryset and
    serializer_class"""
    serializer_class = EmployeeSerialize
    queryset = Employee.objects.all()

    def get_queryset(self):
        """Custom function for working with a filter"""
        queryset = self.queryset
        queryset = queryset.all()
        selected_department = self.request.GET.get("department", None)
        start = self.request.GET.get("start", None)
        end = self.request.GET.get("end", None)
        if selected_department != '' and selected_department is not None:
            id_dep = Department.objects.get(full_name=selected_department).id
            queryset = queryset.filter(department=id_dep)
        if start and end:
            queryset = queryset.filter(date_of_birthday__range=[start, end])
        elif start and not end:
            queryset = queryset.filter(date_of_birthday=start)
        return queryset
