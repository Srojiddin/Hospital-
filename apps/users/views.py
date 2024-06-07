from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_protect

from apps.doctors.models import Doctor
from apps.users.forms import UserCreationForm, UserUpdateForm, UserRegisterForm, UserLoginForm
from django.views.generic import DeleteView, TemplateView
from django.contrib.auth.models import User
from django.views import View


User = get_user_model()


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = Doctor.objects.all()

        return context


class UserCreateView(generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/account.html'
    success_url = '/'


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'users/users_detail.html'
    context_object_name = 'user'


class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/users_update.html'
    context_object_name = 'user'
    success_url = '/profile/'


class UserProfileView(generic.DetailView):
    model = User
    template_name = 'users/user_profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/user_delete.html'
    context_object_name = 'user'
    success_url = '/index.html'


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy('home'))
        return render(request, 'users/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        return render(request, 'users/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')