from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import OrderItem


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя:', widget=forms.TextInput(
        attrs={'class': "form-control",
               'id': "first",
               'name': "name"
               }))
    last_name = forms.CharField(label='Фамилия:', widget=forms.TextInput(
        attrs={'class': "form-control",
               'id': "last",
               'name': "name"
               }))
    email = forms.EmailField(label='Email:', widget=forms.EmailInput(
        attrs={'class': "form-control",
               'id': "email",
               'name': "compemailany"

               }))
    phone_number = forms.CharField(label='Номер телефона:', widget=forms.TextInput(
        attrs={'class': "form-control",
               'id': "number",
               'name': "number"

               }))
    address = forms.CharField(label='Адрес:', widget=forms.TextInput(
        attrs={'class': "form-control",
               'id': "add1",
               'name': "add1"

               }))
    city = forms.CharField(label='Город:', widget=forms.TextInput(
        attrs={'class': "form-control",
               'id': "city",
               'name': "city"

               }))

    country = forms.CharField(label='Страна:', widget=forms.TextInput(
        attrs={'class': "form-control",
               'id': "country",
               'name': "country"
               }))
    zipcode = forms.CharField(label='Зип:', widget=forms.TextInput(
        attrs={'class': "form-control",
               'id': "zip",
               'name': "zip",
               }))

    class Meta:
        model = OrderItem
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'zipcode']