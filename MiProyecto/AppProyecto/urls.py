from django.urls import path
from AppProyecto.presentation.views import login_view

urlpatterns = [
    path('', login_view.login_view, name='login'),  # La página de login como raíz
    path('login/', login_view.login_view, name='login'),  # Puedes mantener esta ruta si es necesario
    # Otras rutas
]