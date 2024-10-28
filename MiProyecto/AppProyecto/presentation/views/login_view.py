from django.shortcuts import render, redirect
from django.contrib import messages
from AppProyecto.business.services.auth_service import authenticate_user

def login_view(request):
    if request.method == 'POST':
        nombre_usuario = request.POST['nombre_usuario']  # Cambiado a nombre_usuario
        contrasena = request.POST['contrasena']          # Cambiado a contrasena
        usuario = authenticate_user(nombre_usuario, contrasena)
        
        if usuario:
            # Aquí realizarías el login usando la sesión de Django
            return redirect('home')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    
    return render(request, 'Login/login.html')