from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.usuario.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'peso']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Escribe tu nombre de usuario'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Escribe tu nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Escribe tu apellido'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
            'peso': forms.NumberInput(attrs={'placeholder': 'Escribe tu peso en números decimales', 'step': '0.01'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Escribe una contraseña'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirma la contraseña'}),
        }

class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'peso']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Escribe tu nombre de usuario'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Escribe tu nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Escribe tu apellido'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
            'peso': forms.NumberInput(attrs={'placeholder': 'Escribe tu peso en números decimales', 'step': '0.01'}),
        }
