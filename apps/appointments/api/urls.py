from django.urls import path, include
from apps.appointments.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.AppointmentCreateView, basename='appointment_api')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/appointment/<int:pk>/', views.AppointmentsUpdateDeleteRetrieveAPIView.as_view(), name='appointment'),
]
