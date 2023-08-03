from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин:', widget=forms.TextInput(
        attrs={'class': "form-control"

               }))
    first_name = forms.CharField(label='Имя:', widget=forms.TextInput(
        attrs={'class': "form-control"

               }))
    last_name = forms.CharField(label='Фамилия:', widget=forms.TextInput(
        attrs={'class': "form-control"

               }))
    email = forms.EmailField(label='Email:', widget=forms.EmailInput(
        attrs={'class': "form-control"

               }))
    password1 = forms.CharField(label='Пароль:', widget=forms.PasswordInput(
        attrs={'class': "form-control"

               }))
    password2 = forms.CharField(label='Повтор пароля:', widget=forms.PasswordInput(
        attrs={'class': "form-control"

               }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': "form-control",
               'placeholder': "Login",
               'id': "name",
               'name': "name",
               'value': ""
               }))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': "form-control",
               'placeholder': "Password",
               'id': "password",
               'name': "password",
               'value': ""
               }))

    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'id': "f-option",
        'name': "selector"
    }))
