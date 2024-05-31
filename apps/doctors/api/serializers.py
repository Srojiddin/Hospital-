from rest_framework import serializers
from apps.doctors.models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class DoctorCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'

