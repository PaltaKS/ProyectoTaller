from django.shortcuts import render
from AppProyecto.models import Usuario  # Importa el modelo si es necesario

def pagina_principal_view(request):
    # Puedes agregar lógica aquí para obtener datos si es necesario
    return render(request, 'Login/home.html')  # Renderiza la plantilla de la página principal