from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreationZakladnikForm(UserCreationForm):
    email = forms.EmailField(label='E-mail')
