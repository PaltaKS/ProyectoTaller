from django.urls import path
from AppProyecto.presentation.views import login_view, home_view

urlpatterns = [
    path('', login_view.login_view, name='login'),  # La página de login como raíz
    path('login/', login_view.login_view, name='login'), # Puedes mantener esta ruta si es necesario
    path('pagina_principal/', home_view.pagina_principal_view, name='pagina_principal'),  # Ruta para la página principal
    # Otras rutas
]