from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path(r"admin/", admin.site.urls), path(r"api/", include("api.urls")),
    path('accounts/', include('allauth.urls')),
]

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
