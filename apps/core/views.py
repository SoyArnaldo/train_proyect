"""Views de la aplicación Core."""

# Django
from django.shortcuts import render, redirect
from apps.ejercicio.models import Comentario

def home(request):
    comentarios = Comentario.objects.all()  
    return render(request, "dashboard/dashboard.html", {'comentarios': comentarios})

