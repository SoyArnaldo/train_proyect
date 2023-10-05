from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserEditForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .models import Item

# @login_required() esto es lo que debe mostrarse en el dashboard
# def video(request):
#     obj=Item.objects.all()
#     return render(request,'index.html', {'obj':obj})


def formulario(request):
    template_user = reverse_lazy('usuario:index')

    if request.user.is_authenticated:
        return HttpResponseRedirect(template_user)
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # Puedes agregar aquí cualquier lógica adicional, como iniciar sesión automáticamente al usuario
            return HttpResponseRedirect(template_user) # Redirige al usuario a la página de inicio de sesión
        else:
            print(form.errors)
            return render(request, 'login/formulario.html', {'form': form})

    else:
        form = CustomUserCreationForm()
        return render(request, 'login/formulario.html', {'form': form})


@login_required()
def editPerfil(request):
    if request.method == 'GET':
        user = request.user
        form = CustomUserEditForm(instance=user)
        return render(request, 'formulario.html', {'form':form})
    
    if request.method == 'POST':
        user = CustomUser.objects.get(username=request.user)
        form = CustomUserEditForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
        else:
            print(form.errors)
            return render(request, 'formulario.html',{'form':form.errors})
        

def autenticationView(request):
    template_name = 'login.html'
    template_user = reverse_lazy('usuario:index')
    
    if request.user.is_authenticated:
        return HttpResponseRedirect(template_user)

    if request.method == 'POST':
       print(request.POST['username'])
       print(request.POST['password'])
       user = authenticate(username=request.POST['username'], password=request.POST['password'])
       print(user)
       if user is not None:
           login(request, user)
           return HttpResponseRedirect(template_user)
       else:
        form = AuthenticationForm()
        return render(request, template_name, {
            'form': form,
            })
        
       
    else:
        form = AuthenticationForm()
        return render(request, template_name, {'form': form})
    

def logOutView(request):
    logout(request)
    
    return HttpResponseRedirect(reverse_lazy('usuario:login'))