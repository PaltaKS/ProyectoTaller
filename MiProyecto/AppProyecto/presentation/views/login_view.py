from django.shortcuts import render, redirect
from django.contrib import messages
from AppProyecto.models import Usuario  # Importa el modelo desde AppProyecto

def login_view(request):
    if request.method == 'POST':  # Verifica si el formulario fue enviado
        nombre_usuario = request.POST['nombre_usuario']  # Obtiene el nombre de usuario
        contrasena = request.POST['contrasena']  # Obtiene la contraseña

        try:
            # Intenta obtener el usuario
            usuario = Usuario.objects.get(nombre_usuario=nombre_usuario, contrasena=contrasena)
            messages.success(request, "Inicio de sesión exitoso.")  # Mensaje de éxito
            return redirect('pagina_principal')  # Redirige a la página principal
        except Usuario.DoesNotExist:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")  # Mensaje de error

    return render(request, 'Login/login.html')  # Renderiza en la plantilla de login
