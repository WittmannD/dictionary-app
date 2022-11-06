"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include
from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view


urlpatterns = [path(r"admin/", admin.site.urls), path(r"api/", include("api.urls"))]

if getattr(settings, "DEBUG", False):
    dev_urlpatterns = [
        path(
            r"swagger/",
            TemplateView.as_view(
                template_name="swagger.html",
                extra_context={"schema_url": "openapi-schema"},
            ),
            name="swagger-ui",
        ),
        path(
            r"openapi/",
            get_schema_view(
                title="dictionary", description="API docs", version="1.0.0"
            ),
            name="openapi-schema",
        ),
    ]

    urlpatterns += dev_urlpatterns
