from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UserCreationForm(UserCreationForm):
    class Meta(UserForm.Meta):
        fields = ['username', 'password1', 'password2']


class UserUpdateForm(UserChangeForm):
    class Meta(UserForm.Meta):
        fields = ['username', 'email', 'first_name', 'last_name']


class UserDetailForm(forms.ModelForm):
    class Meta(UserForm.Meta):
        fields = ['username', 'email', 'first_name', 'last_name']


class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100, label='Имя пользователя')
#     password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')


