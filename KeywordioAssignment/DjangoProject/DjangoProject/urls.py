from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('DjangoApp/', include('DjangoApp.urls')),

    path('LifeEazy/', get_schema_view(
        title="Keywordio",
        # description="API developers hoping to use our service"
    ), name='openapi-schema'),
    path('', TemplateView.as_view(
        template_name='index.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    # path('',schema_view)
]