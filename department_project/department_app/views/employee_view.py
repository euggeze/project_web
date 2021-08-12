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
        selected_department = self.request.GET.get("department", None)
        if selected_department != '' and selected_department is not None:
            id_dep = Department.objects.get(full_name=selected_department).id
            query_set = queryset.filter(department=id_dep)
            return query_set
        query_set = queryset.all()
        return query_set
