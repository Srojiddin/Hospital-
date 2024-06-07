from django.urls import path
from apps.appointments.views import AppointmentList, AppointmentCreate, AppointmentDetail, AppointmentUpdate, AppointmentDelete, ContactListView


urlpatterns = [
    path('appointment/', AppointmentList.as_view(), name='appointment-list'),
    path('create/appointments', AppointmentCreate.as_view(), name='create-appointments'),
    path('appointments/<int:pk>/', AppointmentDetail.as_view(), name='appointment-detail'),
    path('appointments/<int:pk>/update/', AppointmentUpdate.as_view(), name='appointment-update'),
    path('appointments/<int:pk>/delete/', AppointmentDelete.as_view(), name='appointment-delete'),
    path('contact/',ContactListView.as_view(), name='contact')
]
