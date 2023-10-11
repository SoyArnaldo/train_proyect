from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserEditForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser

def registro(request):
    template_user = reverse_lazy('usuario:login') #se define el template user con reverse

    if request.user.is_authenticated: #si el user ya esta registrado, lo lleva al login
        return HttpResponseRedirect(template_user)
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES) #se incluyen las imagenes
        if form.is_valid():
            user = form.save()
            # Se puede agregar aquí cualquier lógica adicional, como iniciar sesión automáticamente al usuario
            return HttpResponseRedirect(template_user) # Redirige al usuario a la página de inicio de sesión
        else:
            print(form.errors)
            return render(request, 'login/registro.html', {'form': form}) #se señala asi porque esta en esa carpeta el registro.html
    else:
        form = CustomUserCreationForm()
        return render(request, 'login/registro.html', {'form': form})


@login_required()
def editPerfil(request):
    # Verificamos si la solicitud HTTP es un GET
    if request.method == 'GET':
        # Obtenemos el usuario actualmente autenticado
        user = request.user
        # Creamos una instancia del formulario de edición de usuario y lo poblamos con los datos del usuario
        form = CustomUserEditForm(instance=user)
        # Renderizamos la plantilla 'login/registro.html' y pasamos el formulario como contexto
        return render(request, 'login/registro.html', {'form': form})

    # Si la solicitud HTTP es un POST (se envió el formulario)
    if request.method == 'POST':
        # Obtenemos el usuario actualmente autenticado
        user = CustomUser.objects.get(username=request.user)
        # Creamos una instancia del formulario de edición de usuario con los datos recibidos en la solicitud POST
        form = CustomUserEditForm(request.POST, instance=user)
        # Verificamos si el formulario es válido
        if form.is_valid():
            # Guardamos los cambios en el usuario
            form.save()
            # Redirigimos al usuario a la página 'index.html'
            return render(request, 'index.html')
        else:
            # Si el formulario no es válido, imprimimos los errores en la consola y mostramos los errores en la plantilla 'login/registro.html'
            print(form.errors)
            return render(request, 'login/registro.html', {'form': form.errors})


def autenticationView(request):
    # Definimos el nombre de la plantilla para el formulario de inicio de sesión
    template_name = 'login/login.html'
    # Definimos la URL de redirección después del inicio de sesión exitoso
    template_user = reverse_lazy('ejercicio:index')
    
    # Verificamos si el usuario ya está autenticado; si es así, lo redirigimos a la página 'index.html'
    if request.user.is_authenticated:
        return HttpResponseRedirect(template_user)

    # Si la solicitud HTTP es un POST (se envió el formulario de inicio de sesión)
    if request.method == 'POST':
        # Obtenemos el nombre de usuario y la contraseña de la solicitud POST
        username = request.POST['username']
        password = request.POST['password']
        # Autenticamos al usuario utilizando las credenciales proporcionadas
        user = authenticate(username=username, password=password)
        
        # Verificamos si la autenticación fue exitosa
        if user is not None:
            # Iniciamos sesión para el usuario autenticado
            login(request, user)
            # Redirigimos al usuario a la página 'index.html'
            return HttpResponseRedirect(template_user)
        else:
            # Si la autenticación falla, creamos una instancia del formulario de autenticación y mostramos los errores
            form = AuthenticationForm(request.POST)
            return render(request, template_name, {
                'form': form,
            })
    else:
        # Si la solicitud HTTP no es un POST, creamos una instancia del formulario de autenticación vacío
        form = AuthenticationForm()
        return render(request, template_name, {'form': form})

def logOutView(request):
    logout(request)
    
    return HttpResponseRedirect(reverse_lazy('usuario:login'))

