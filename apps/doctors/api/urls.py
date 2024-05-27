from django.urls import path
from apps.doctors.api import views

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('doctors/create/', DoctorCreateAPIView.as_view(), name='doctor_create'),
    path('doctors/', DoctorListAPIView.as_view(), name='doctor_list'),
    path('doctors/<int:pk>/', DoctorDetailAPIView.as_view(), name='doctor_detail'),
    path('doctors/update/<int:pk>/', DoctorUpdateAPIView.as_view(), name='doctor_update'),
    path('doctors/delete/<int:pk>/', DoctorDeleteAPIView.as_view(), name='doctor_delete'),
]