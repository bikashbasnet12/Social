from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class RegisteruserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","username","email","password"]

class LoginUserForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'border border-gray-300 rounded px-3 py-2 w-max focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Username',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border border-gray-300 rounded px-3 py-2 w-max focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Password',
        })
    )