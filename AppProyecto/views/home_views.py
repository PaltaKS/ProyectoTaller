from django.shortcuts import render, redirect
from AppProyecto.models import Usuario

def home_view(request):
    user_id = request.session.get('user_id')  # Obtener el ID del usuario de la sesión
    if user_id:
        try:
            usuario = Usuario.objects.get(id_usuario=user_id)  # Asegúrate de usar 'id_usuario' aquí
        except Usuario.DoesNotExist:
            usuario = None  # Manejar el caso en que el usuario no se encuentra
            return redirect('login')  # Redirigir si el usuario no está

        return render(request, 'home.html', {'usuario': usuario})  # Cambia aquí a 'usuario'
    else:
        return redirect('login')
    


def procedimiento_almacenado(request):
    return render(request, 'ProcidimientosAlmacenados\procedimiento_home.html')
