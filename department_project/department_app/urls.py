"""The `urlpatterns` list routes URLs to views for department_app"""
from rest_framework.routers import SimpleRouter

from department_app.views import employee_view, department_view

router = SimpleRouter()
router.register("employee", employee_view.EmployeeViewSet, basename='employee')
router.register("department", department_view.DepartmentViewSet, basename='department')

urlpatterns = router.urls
