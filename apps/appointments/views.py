from django.shortcuts import render
from django.views import generic
from apps.appointments.models import Appointment
from apps.appointments.forms import AppointmentCreateFrom, AppointmentDetailForm, AppointmentDeleteForm
from django.urls import reverse_lazy
from apps.appointments.models import Appointment, Doctor, Category

class AppointmentList(generic.ListView):
    model = Appointment
    template_name = 'appointments/contact.html'
    context_object_name = 'appointments_list'




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


class AppointmentCreate(generic.CreateView):
    model = Appointment
    form_class = AppointmentCreateFrom
    template_name = 'contact.html' 
   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['select doctor'] = Appointment.objects.all()
        context['select departments'] = Appointment.objects.all()
        print("*" * 30)

        return context





def create_appointments(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('your_phone_number')
        doctor_id = request.POST.get('choosing_a_doctor')
        disease_id = request.POST.get('choosing_a_disease')
        date_of_reservation = request.POST.get('date_of_reservation')

        appointment = Appointment.objects.create(
            full_name=full_name,
            your_phone_number=phone_number,
            choosing_a_doctor_id=doctor_id,
            choosing_a_disease_id=disease_id,
            date_of_reservation=date_of_reservation
        )
        Appointment.save()

        return render(request, 'confirmation.html', {'appointment': appointment})
    else:

        doctors = Doctor.objects.all()
        categories = Category.objects.all()
        return render(request, 'create_appointments.html', {'doctors': doctors, 'categories': categories})
