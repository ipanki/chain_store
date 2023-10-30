from django.urls import include, path
from rest_framework_nested import routers

from applications.companies import views

router = routers.DefaultRouter()
router.register('companies', views.CompanyViewSet, 'companies')
domain_router = routers.NestedSimpleRouter(
    router, 'companies', lookup='companies')
domain_router.register('products', views.CompanyProductViewSet, 'products')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(domain_router.urls)),
]
