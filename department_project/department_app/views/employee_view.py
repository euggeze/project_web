"""Module for working with Employee model"""
from django.db.models import QuerySet
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
        assert self.queryset is not None, (
                "'%s' should either include a `queryset` attribute, "
                "or override the `get_queryset()` method."
                % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
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
