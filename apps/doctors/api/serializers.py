from rest_framework import serializers
from apps.doctors.models import Doctor


class DoctorCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['name', 'lastname', 'age', 'image_for_doctor', 'choosing_a_specialization', 'experience', 'creation_date']


class DoctorDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['name', 'lastname', 'age', 'choosing_a_specialization', 'creation_date']


class DoctorUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['name', 'lastname', 'age', 'choosing_a_specialization', 'experience', 'creation_date']


class DoctorDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = []
