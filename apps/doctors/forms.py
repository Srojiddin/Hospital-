from django import forms
from apps.doctors.models import Doctor


class DoctorCreateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'lastname', 'age', 'image_for_doctor', 'choosing_a_specialization', 'experience', 'creation_date']


class DoctorDetailForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'lastname', 'age', 'choosing_a_specialization', 'creation_date']


class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'lastname', 'age', 'choosing_a_specialization', 'experience', 'creation_date']


class DoctorDeleteForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = []
