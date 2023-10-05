"""Views de la aplicación Core."""

# Django
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect



def home(request):
    """Vista de la página de inicio."""

    return render(request, "dashboard/dashboard.html")
