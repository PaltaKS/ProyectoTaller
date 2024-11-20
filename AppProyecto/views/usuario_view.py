# AppProyecto/views/usuario_views.py
from django.shortcuts import render, redirect, get_object_or_404
from AppProyecto.models import Usuario, Rol, Trabajador
from AppProyecto.services.usuario_service import UsuarioService
from AppProyecto.repositories.usuario_repository import UsuarioRepository

# Listar Usuarios
def listar_usuarios(request):
    usuarios = UsuarioService.listar_usuarios()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})

# Crear Usuario
def crear_usuario(request):
    # Obtener datos para los select del formulario
    trabajadores = UsuarioRepository.obtener_todos_los_trabajadores()
    roles = UsuarioRepository.obtener_todos_los_roles()
    
    if request.method == 'POST':
        # Recibir datos del formulario
        nombre_usuario = request.POST.get('nombre_usuario')
        trabajador_id = request.POST.get('trabajador')
        rol_id = request.POST.get('rol')
        email = request.POST.get('email')
        contrasena = request.POST.get('contrasena')
        
        # Delegar la creación de usuario al servicio
        UsuarioService.crear_usuario(
            nombre_usuario=nombre_usuario,
            trabajador_id=trabajador_id,
            rol_id=rol_id,
            email=email,
            contrasena=contrasena
        )
        return redirect('lista_usuarios')  # Redirigir a la lista de usuarios
    
    return render(request, 'usuarios/formulario.html', {'trabajadores': trabajadores, 'roles': roles})

# Actualizar Usuario
def actualizar_usuario(request, id_usuario):
    usuario = UsuarioRepository.obtener_por_id(id_usuario)  # Obtener el usuario existente
    trabajadores = UsuarioRepository.obtener_todos_los_trabajadores()
    roles = UsuarioRepository.obtener_todos_los_roles()

    if request.method == 'POST':
        # Recibir datos del formulario
        nombre_usuario = request.POST.get('nombre_usuario')
        trabajador_id = request.POST.get('trabajador')
        rol_id = request.POST.get('rol')
        email = request.POST.get('email')
        contrasena = request.POST.get('contrasena')

        # Delegar la actualización al servicio
        UsuarioService.actualizar_usuario(
            id_usuario=id_usuario,
            nombre_usuario=nombre_usuario,
            trabajador_id=trabajador_id,
            rol_id=rol_id,
            email=email,
            contrasena=contrasena
        )
        return redirect('lista_usuarios')  # Redirigir a la lista de usuarios

    return render(request, 'usuarios/formulario.html', {'usuario': usuario,'trabajadores': trabajadores,'roles': roles,})

# Eliminar Usuario
def eliminar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, pk=id_usuario)  # Obtener el usuario o mostrar un 404 si no existe

    if request.method == 'POST':
        UsuarioService.eliminar_usuario(id_usuario)  # Llamar al servicio para eliminar el usuario
        return redirect('lista_usuarios')  # Redirigir a la lista después de eliminar

    # Si el método es GET, mostramos una página de confirmación
    return render(request, 'usuarios/eliminar.html', {'usuario': usuario})
