from rest_framework.routers import SimpleRouter

from department_app.views import employee_view,department_view


router = SimpleRouter()
router.register("employee", employee_view.EmployeeInfoViewSet)
router.register("department", department_view.DepartmentInfoViewSet)

urlpatterns = router.urls
