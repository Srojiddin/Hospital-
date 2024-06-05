from django.urls import path, include
from apps.users.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register('users', views.UsersCreateViewSet, basename="users_api")




urlpatterns = [
   path('users/<int:pk>/', views.DoctorUpdateDeleteRetrieveAPIView.as_view(), name='user'),
   path('api/', include(router.urls)),
]

