
from rest_framework import generics, viewsets


from apps.doctors.models import Doctor
from apps.doctors.api.serializers import DoctorSerializer, DoctorCreateSerializer

from utils.permissions import IsAdmin


class DoctorCreateViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorCreateSerializer
    permission_classes = [IsAdmin]

    def get_serializer_class(self):
        if self.action in ['create']:
            return DoctorCreateSerializer
        elif self.action == 'retrieve':
            return DoctorSerializer
        return self.serializer_class


class DoctorUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAdmin]


