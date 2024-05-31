from django import forms
from apps.appointments.models import Appointment


class AppointmentCreateFrom(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentDetailForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentDeleteForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'




