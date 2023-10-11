from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import ComentarioForm 
from django.contrib.auth.decorators import login_required
from .models import Item, Comentario as ComentarioModel  

@login_required
def video(request):
    obj = Item.objects.all()
    comentario_form = ComentarioForm()  # Utiliza el formulario con el nuevo nombre

    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario_text = comentario_form.cleaned_data['comentario']

            # Instancia para guardar los comentarios en la bd
            comentario = ComentarioModel(comentario=comentario_text)  # Utiliza el modelo con el nuevo nombre
            comentario.save()

    return render(request, 'dashboard/index.html', {'obj': obj, 'comentario_form': comentario_form})
