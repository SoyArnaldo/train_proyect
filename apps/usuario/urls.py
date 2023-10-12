from django.urls import path     
from .views import  registro, autenticationView, logOutView, editPerfil
from config import settings
from django.conf.urls.static import static



app_name = 'usuario'

urlpatterns = [
    path(route='registro/', view=registro, name='registro'), 
    path(route='accounts/login/', view=autenticationView, name='login'),
    path(route='logout', view=logOutView, name='logout'),
    path('edit/', view= editPerfil, name='editPerfil')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
