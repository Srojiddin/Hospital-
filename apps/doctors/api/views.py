from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

from apps.doctors.models import Doctor
from apps.doctors.serializers import DoctorCreateSerializer, DoctorDetailSerializer, DoctorUpdateSerializer, DoctorDeleteSerializer


class Homepage(APIView):

    def get(self, request, format=None):
        doctors = Doctor.objects.all()
        serializer = DoctorDetailSerializer(doctors, many=True)
        return Response(serializer.data)

class DoctorCreateAPIView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DoctorListAPIView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DoctorDetailAPIView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DoctorUpdateAPIView(generics.UpdateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DoctorDeleteAPIView(generics.DestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDeleteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

