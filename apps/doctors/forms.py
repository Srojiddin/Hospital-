from django import forms
from apps.doctors.models import Doctor

class DoctorBaseForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'lastname', 'age', 'image_for_doctor', 'choosing_a_specialization', 'experience', 'creation_date']

class DoctorCreateForm(DoctorBaseForm):
    pass

class DoctorDetailForm(DoctorBaseForm):
    class Meta(DoctorBaseForm.Meta):
        fields = ['name', 'lastname', 'age', 'image_for_doctor', 'choosing_a_specialization', 'creation_date']

class DoctorUpdateForm(DoctorBaseForm):
    pass

class DoctorDeleteForm(DoctorBaseForm):
    pass
