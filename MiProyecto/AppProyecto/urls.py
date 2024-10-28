from django.urls import path
from AppProyecto.presentation.views import login_view, home_view
from AppProyecto.presentation.views.home_view import custom_logout_view
from AppProyecto.presentation.views import home_view, trabajador_view

urlpatterns = [
    path('', login_view.login_view, name='login'),  # La página de login como raíz
    path('login/', login_view.login_view, name='login'), # Puedes mantener esta ruta si es necesario
    path('pagina_principal/', home_view.pagina_principal_view, name='pagina_principal'), # Ruta para la página principal
    path('logout/', custom_logout_view, name='logout'),
    path('Trabajadores_Home', home_view.trabajadores_home, name='trabajadores_home'),  # Ruta para la página de inicio
    path('trabajadores/', trabajador_view.trabajador_list, name='trabajador_list'),  
    path('trabajadores/crear/', trabajador_view.trabajador_create, name='trabajador_create'),
    path('trabajadores/editar/<int:id_trabajador>/', trabajador_view.trabajador_update, name='trabajador_update'),
    path('trabajadores/eliminar/<int:id_trabajador>/', trabajador_view.trabajador_delete, name='trabajador_delete'),
    path('trabajadores/home/', home_view.trabajadores_home, name='trabajadores_home'),  # Ruta para el home de trabajadores
    # Otras rutas
]