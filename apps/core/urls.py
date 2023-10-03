"""URLs de la aplicación Core."""

# Django
from django.urls import path

# Views (son funciones)
from apps.core.views import home, formulario, registro

# Es para evitar conflictos con otras aplicaciones, en caso de que tengamos
# una vista con el mismo nombre.
app_name = 'core'
urlpatterns = [
	path(route='', view=home, name='home'),  # está vacío porque es la página principal
	path(route='formulario/', view=formulario, name='formulario'),  # está vacío porque es la página principal
	path(route='registro/', view=registro, name='registro'),  # está vacío porque es la página principal
]
