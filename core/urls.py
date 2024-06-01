from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from core.admin import admin

api_urlpatterns = [
    path('doctors/', include('apps.doctors.api.urls')),
    path('comments/', include('apps.comments.api.urls')),
    path('appointments/', include('apps.appointments.api.urls')),
    path('category/', include('apps.categories.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.doctors.urls')),
    path('', include('apps.users.urls')),
    path('', include('apps.appointments.urls')),
    path('', include('apps.categories.urls')),
    path('', include('apps.comments.urls')),
]
urlpatterns += api_urlpatterns


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
