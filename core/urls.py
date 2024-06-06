from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from core.admin import admin
from core.swagger import docs

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

api_urlpatterns = [
    path('api/', include('apps.doctors.api.urls')),
    path('api/',include('apps.users.api.urls')),
    path('api/', include('apps.appointments.api.urls')),
    path('api/', include('apps.categories.api.urls')),
    path('api/', include('apps.blogs.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('token_create/', TokenObtainPairView.as_view()),
    path('token_refresh/', TokenRefreshView.as_view()),
    path('docs/', docs.with_ui('swagger', cache_timeout=0), name="docs"),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.doctors.urls')),
    path('', include('apps.users.urls')),
    path('', include('apps.appointments.urls')),
    path('', include('apps.categories.urls')),
    path('', include('apps.blogs.urls'))
]
urlpatterns += api_urlpatterns


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
