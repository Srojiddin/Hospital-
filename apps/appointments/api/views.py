from rest_framework import viewsets, generics
from apps.appointments.api.serializers import AppointmentSerializer, AppointmentCreateSerializer
from apps.appointments.models import Appointment


class AppointmentCreateView(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            return AppointmentCreateSerializer
        elif self.action == 'retrieve':
            return AppointmentSerializer
        return AppointmentSerializer


class AppointmentsUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer



