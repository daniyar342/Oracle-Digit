from django.urls import path
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView



SPECTACULAR_SETTINGS = {
    'TITLE': 'Ваше API',
    'DESCRIPTION': 'Описание вашего API',
    'VERSION': '1.0.0',
}
urlpatterns = [
    # Сгенерировать саму схему
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # ReDoc
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]