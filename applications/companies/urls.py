from django.urls import include, path
from rest_framework_nested import routers

from applications.companies import views

router = routers.DefaultRouter()
router.register('companies', views.CompanyViewSet, 'companies')
router.register(
    'companies/(?P<company_id>[^/.]+)/products', views.CompanyProductViewSet, 'products')
router.register(
    'companies/(?P<company_id>[^/.]+)/employees', views.EmployeeViewSet, 'employees')

urlpatterns = [
    path('', include(router.urls))
]
