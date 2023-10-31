"""chain_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from applications import urls

v1_urls = [
    path('', include('applications.authentication.urls')),
    path('', include('applications.companies.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(v1_urls)),
]

if settings.DEBUG:
    urlpatterns += [
        path('swagger(?P\.json|\.yaml)', urls.schema_view.without_ui(
            cache_timeout=0), name='schema-json'),
        path('swagger/', urls.schema_view.with_ui('swagger',
             cache_timeout=0), name='schema-swagger-ui')
    ]
