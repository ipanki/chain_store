from rest_framework import routers
from applications.authentication import views

router = routers.DefaultRouter()
router.register('auth', views.RegistrationViewSet, 'auth')

urlpatterns = router.urls
