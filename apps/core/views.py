"""Views de la aplicación Core."""

# Django
from django.shortcuts import render, redirect
from apps.usuario.models import CustomUser
from apps.ejercicio.models import Comentario

def home(request):
    users = CustomUser.objects.all()
    userComm = None
    for user in users:
        userComm = user
    coments = Comentario.objects.filter(user=userComm)
    context = {
        "users": users,
        "coments": coments
        }
    return render(request, "dashboard/dashboard.html",context)

