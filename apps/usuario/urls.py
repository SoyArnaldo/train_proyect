from django.urls import path     
from . import views #means that views is in the same directory as this
from .views import  registro #video,


app_name = 'usuario'

urlpatterns = [
    # path('', views.video, name='index'), este es el que muestra los videos hina
    path(route='registro/', view=registro, name='registro'), 
    path('login', views.autenticationView, name='login'),
    path('logout', views.logOutView, name='logout'),
    path('edit', views.editPerfil, name='editPerfil')
    
]
