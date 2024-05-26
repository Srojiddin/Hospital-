from django.urls import path

from apps.users.views import UserCreateView, UserDetailView, UserUpdateView,UserDeleteView
# from apps.users.views import signup_logics, login_logics, logout_logics

urlpatterns = [
    path('user/list/', UserCreateView.as_view(), name='login.html'),
    path('user/detail/', UserDetailView.as_view(), name='user_detail'),
    path('user/detail/', UserUpdateView.as_view(), name='user_update'),
    path('user/delete/', UserDeleteView.as_view(), name='user_delete'),
    # path('login/', login_logics, name='login'),
    # path('sign_up/', signup_logics, name='sign_up'),
    # path('logout/', logout_logics, name='logout'),
]
