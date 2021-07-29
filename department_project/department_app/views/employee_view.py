from rest_framework.response import Response
from rest_framework.views import APIView

from department_app.models import Employee
from department_app.rest.serializers import EmployeeSerialize


class GetEmployeeInfoView(APIView):
    def get(self, request):
        # Получаем набор всех записей из таблицы
        queryset = Employee.objects.all()
        # Сериализуем извлечённый набор записей
        serializer_for_queryset = EmployeeSerialize(
            instance=queryset,  # Передаём набор записей
            many=True  # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)
