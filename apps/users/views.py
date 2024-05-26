from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
from apps.users.forms import UserCreationForm, UserUpdateForm
from django.views.generic import DeleteView
from django.contrib.auth.models import User
from django.views import View


User = get_user_model()


class UserCreateView(generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/account.html'
    success_url = '/index.html'


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'users_detail.html'
    context_object_name = 'user'


class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users_update.html'
    context_object_name = 'user'
    success_url = '/index.html'


class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_delete.html'
    context_object_name = 'user'
    success_url = '/index.html'


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserManager:
    def __init__(self):
        self.users = []

    def register(self, username, password):
        if self.find_user(username) is None:
            self.users.append(User(username, password))
            print(f"Пользователь {username} успешно зарегистрирован.")
        else:
            print("Пользователь с таким именем уже существует.")

    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def authenticate(self, username, password):
        user = self.find_user(username)
        if user is not None and user.password == password:
            print(f"Пользователь {username} успешно авторизован.")
        else:
            print("Неверное имя пользователя или пароль.")


# userManager = UserManager()
# userManager.register("user1", "password1")
# userManager.authenticate("user1", "password1")
# userManager.authenticate("user1", "password2")
