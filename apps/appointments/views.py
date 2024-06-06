from django.views import generic
from apps.appointments.models import Appointment
from apps.appointments.forms import AppointmentCreateFrom, AppointmentDetailForm, AppointmentDeleteForm
from django.urls import reverse_lazy


class AppointmentList(generic.ListView):
    model = Appointment
    template_name = 'appointments/contact.html'
    context_object_name = 'appointments_list'


class AppointmentCreate(generic.CreateView):
    model = Appointment
    form_class = AppointmentCreateFrom
    template_name = 'appointments/appointment_form.html' 


class AppointmentDetail(generic.DetailView):
    model = Appointment
    form_class = AppointmentDetailForm
    template_name = 'appointments/appointment_detail.html'
    context_object_name = 'appointment'


class AppointmentUpdate(generic.UpdateView):
    model = Appointment
    template_name = 'appointments/appointment_update.html'
    form_class = AppointmentDetailForm


class AppointmentDelete(generic.DeleteView):
    model = Appointment
    form_class = AppointmentDeleteForm
    template_name = 'appointments/appointment_confirm_delete.html'
    context_object_name = 'appointment'
    success_url = reverse_lazy('/')


class ContactListView(generic.ListView):
    model = Appointment
    template_name = 'contact.html'

