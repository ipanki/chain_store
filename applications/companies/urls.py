from django.urls import include, path
from rest_framework_nested import routers

from applications.companies import views

router = routers.DefaultRouter()
router.register('companies', views.CompanyViewSet, 'companies')
router.register('products', views.CompanyProductViewSet, 'products')
router.register('employees', views.EmployeeViewSet, 'employees')

urlpatterns = [
    path('', include(router.urls))
]
