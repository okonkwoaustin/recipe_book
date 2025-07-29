from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistionForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    phone_no = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ["username", "email", "phone_no", "password1", "password2"]