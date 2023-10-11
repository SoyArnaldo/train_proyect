from django import forms
from apps.ejercicio.models import Comentario

class ComentarioForm(forms.Form):
    comentario = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Deja un comentario sobre tu experiencia en la página'}),
        required=False
    )
