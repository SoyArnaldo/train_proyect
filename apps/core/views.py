"""Views de la aplicación Core."""

# Django
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect



def home(request):
    """Vista de la página de inicio."""

    return render(request, "dashboard/dashboard.html")

def formulario(request):
    return render(request, "login/formulario.html")

@csrf_protect
def registro(request):
    print(request)
    return redirect(home)
