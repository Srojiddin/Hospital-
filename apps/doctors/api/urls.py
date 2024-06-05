from django.urls import path, include
from apps.doctors.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.DoctorCreateViewSet, basename="doctor_api")


urlpatterns = [
   path('doctor/<int:pk>/', views.DoctorUpdateDeleteRetrieveAPIView.as_view(), name='doctor'),
   path('api/', include(router.urls)),
]

