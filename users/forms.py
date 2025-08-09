from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import customuser

class UserRegistionForm(UserCreationForm):
    class Meta:
       model = customuser
       fields = ("email", "first_name", "last_name",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = customuser
        fields = ("email", "first_name", "last_name",)
        