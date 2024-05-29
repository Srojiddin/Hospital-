from django.urls import path

from apps.doctors.views import DoctorCreateView, DoctorListView, DoctorDetailView, DoctorUpdateView, DoctorDeleteView, \
    HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('doctor/create/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctor/list/', DoctorListView.as_view(), name='doctor_list'),
    path('doctor/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('doctor/update/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctor/delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),
]

