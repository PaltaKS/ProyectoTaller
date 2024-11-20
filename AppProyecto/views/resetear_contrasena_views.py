from django.shortcuts import render, redirect
from AppProyecto.services.usuario_service import UsuarioService

def recuperar_contrasena(request):
    mensaje_exito = ''
    mensaje_error = ''
    
    if request.method == 'POST':
        email = request.POST.get('email')
        
        if not email:
            mensaje_error = "Por favor ingresa un correo electrónico."
        else:
            if UsuarioService.enviar_correo_recuperacion(email):
                mensaje_exito = "Correo enviado con éxito. Revisa tu bandeja de entrada."
            else:
                mensaje_error = "No se encontró un usuario con ese correo."
    
    # Pasamos los mensajes a la plantilla
    return render(request, 'RecuperarContrasena/solicitar_recuperacion.html', {
        'mensaje_exito': mensaje_exito,
        'mensaje_error': mensaje_error
    })

def restablecer_contrasena(request, token):
    mensaje_exito = ''
    mensaje_error = ''
    
    if request.method == 'POST':
        nueva_contrasena = request.POST.get('new_password')
        
        if not nueva_contrasena:
            mensaje_error = "Por favor ingresa una nueva contraseña."
        else:
            if UsuarioService.restablecer_contrasena(token, nueva_contrasena):
                mensaje_exito = "Contraseña restablecida con éxito."
            else:
                mensaje_error = "Token inválido o expirado."
    
    # Pasamos los mensajes a la plantilla
    return render(request, 'RecuperarContrasena/restablecer_contrasena.html', {
        'mensaje_exito': mensaje_exito,
        'mensaje_error': mensaje_error,
        'token': token
    })

