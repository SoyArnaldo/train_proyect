from django.urls import path     
from .views import video

app_name = 'ejercicio'

urlpatterns = [
    path(route='index/', view=video, name='index'),
    
]