from rest_framework import generics,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

from apps.doctors.models import Doctor
from apps.doctors.api.serializers import DoctorSerializer, DoctorCreateSerializer


class DoctorCreateViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorCreateSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return DoctorCreateSerializer
        elif self.action == 'retrieve':
            return DoctorSerializer
        return self.serializer_class


class DoctorUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


