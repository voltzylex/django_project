from django.urls import include, path
from rest_framework import routers
from api.views import CompanyViewSet, EmployeeViewSEt
router = routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'employee',EmployeeViewSEt)

urlpatterns = [
  path("",include(router.urls)),
  path("",include(router.urls))
]
