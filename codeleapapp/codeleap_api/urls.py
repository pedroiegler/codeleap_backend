from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

# Swagger:
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="CodeLeap Careers API",
      default_version='v1',
      description="API para teste técnico Backend CodeLeap",
      contact=openapi.Contact(email="pedroiegler1601@outlook.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('careers.urls')),

    # Swagger URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]