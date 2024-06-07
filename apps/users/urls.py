from django.urls import path

from apps.users.views import (
    UserCreateView, UserDetailView, UserUpdateView, UserDeleteView, RegisterView, logout_view, UserProfileView, IndexView, LoginView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('logout/', logout_view, name='logout'),
    path('user/list/', UserCreateView.as_view(), name='user_list'),
    path('user/detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]
