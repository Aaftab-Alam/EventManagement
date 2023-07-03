from django import forms
from .models import Users


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'


class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['email', 'password']
