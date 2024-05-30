from django.contrib.auth.views import LoginView
from django.urls import path

from apps.users.views import (
    UserCreateView, UserDetailView, UserUpdateView, UserDeleteView, RegisterView, logout_view, UserProfileView, HomeView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('logout/', logout_view, name='logout'),
    path('user/list/', UserCreateView.as_view(), name='user_list'),
    path('user/detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]
