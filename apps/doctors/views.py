from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views import View
from apps.doctors.models import Doctor
from apps.doctors.forms import DoctorCreateForm, DoctorUpdateForm, DoctorDeleteForm


class DoctorCreateView(generic.CreateView):
    model = Doctor
    form_class = DoctorCreateForm
    template_name = 'doctors/doctor_create.html'
    success_url = reverse_lazy('doctors.list')
    # context_object_name = "doctors"


class DoctorListView(generic.ListView):
    model = Doctor
    template_name = 'doctors.html'
    context_object_name = "doctors"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DoctorCreateForm()
        return context


class DoctorDetailView(generic.DetailView):
    model = Doctor
    template_name = 'doctors/doctor_detail.html'
    context_object_name = 'doctors'


class DoctorUpdateView(generic.UpdateView):
    model = Doctor
    form_class = DoctorUpdateForm
    template_name = 'doctors/doctor_update.html'
    success_url = 'doctors.html'


class DoctorDeleteView(generic.DeleteView):
    model = Doctor
    form_class = DoctorDeleteForm
    template_name = 'doctors/doctor_delete.html'
    context_object_name = 'object'
    success_url = 'doctors.html'

