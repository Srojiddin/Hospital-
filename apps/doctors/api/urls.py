from django.urls import path
from apps.doctors.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.DoctorCreateViewSet, basename="doctor_api")


urlpatterns = [
   path('doctor/<int:pk>/', views.DoctorUpdateDeleteRetrieveAPIView.as_view(), name='doctor'),
]

    # path('doctors/', DoctorListAPIView.as_view(), name='doctor_list'),
    # path('doctors/<int:pk>/', DoctorDetailAPIView.as_view(), name='doctor_detail'),
    # path('doctors/update/<int:pk>/', DoctorUpdateAPIView.as_view(), name='doctor_update'),
    # path('doctors/delete/<int:pk>/', DoctorDeleteAPIView.as_view(), name='doctor_delete'),

urlpatterns += router.urls