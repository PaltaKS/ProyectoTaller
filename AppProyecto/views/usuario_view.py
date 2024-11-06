from django.shortcuts import render, redirect, get_object_or_404
from AppProyecto.models import Usuario, Rol, Trabajador

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})

def crear_usuario(request):
    trabajadores = Trabajador.objects.all()  # Obtener todos los trabajadores
    roles = Rol.objects.all()  # Obtener todos los roles
    if request.method == 'POST':
        # Aquí deberías manejar la creación del usuario
        usuario = Usuario()
        usuario.nombre_usuario = request.POST.get('nombre_usuario')
        usuario.trabajador_id = request.POST.get('trabajador')  # Asignar el trabajador
        usuario.rol_id = request.POST.get('rol')  # Asignar el rol
        usuario.contrasena = request.POST.get('contrasena')
        usuario.save()
        return redirect('lista_usuarios')
    return render(request, 'usuarios/formulario.html', {'roles': roles, 'trabajadores': trabajadores})

def actualizar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    trabajadores = Trabajador.objects.all()  # Obtener todos los trabajadores
    roles = Rol.objects.all()  # Obtener todos los roles
    if request.method == 'POST':
        usuario.nombre_usuario = request.POST.get('nombre_usuario')
        usuario.trabajador_id = request.POST.get('trabajador')  # Asignar el trabajador
        usuario.rol_id = request.POST.get('rol')  # Asignar el rol
        contrasena = request.POST.get('contrasena')
        if contrasena:  # Solo actualizar si se ha proporcionado una nueva contraseña
            usuario.contrasena = contrasena
        usuario.save()
        return redirect('lista_usuarios')
    return render(request, 'usuarios/formulario.html', {'usuario': usuario, 'roles': roles, 'trabajadores': trabajadores})

def eliminar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)

    if request.method == 'POST':
        usuario.delete()  # Eliminar el usuario
        return redirect('lista_usuarios')  # Redirigir a la lista de usuarios

    return render(request, 'usuarios/eliminar.html', {'usuario': usuario})
