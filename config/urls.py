from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import swagger

product = ([
               path('', include('apps.products.urls')),
           ], 'product')

user = ([
               path('', include('apps.users.urls'))
           ], 'user')

v1 = ([
          path('product/', include(product)),
          path('user/', include(user))

      ], 'v1')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(v1)),
]

urlpatterns += swagger.urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
