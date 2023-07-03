from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Checkout,Houses
from django import forms

class CreateUser(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password1',
            'password2',
        ]

class Checkoutinputs(forms.ModelForm):
    class Meta:
        model=Checkout
        fields='__all__'
        widgets={
            'amount':forms.TextInput(attrs={'placeholder':'Enter amount of the house'}),
            }

class Houses_adding(forms.ModelForm):
    class Meta:
        model=Houses
        fields='__all__'