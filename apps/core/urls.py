"""URLs de la aplicación Core."""

# Django
from django.urls import path, include

# Views (son funciones)
from apps.core.views import home

# Es para evitar conflictos con otras aplicaciones, en caso de que tengamos
# una vista con el mismo nombre.
app_name = 'core'
urlpatterns = [
	path(route='', view=home, name='home'),
    path('usuario/', include('apps.usuario.urls')),  # Incluye las URLs de 'apps.usuario'
]
