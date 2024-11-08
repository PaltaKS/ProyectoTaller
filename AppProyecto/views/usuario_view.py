from django.shortcuts import render, redirect, get_object_or_404
from AppProyecto.models import Usuario, Rol, Trabajador
from AppProyecto.services.usuario_service import UsuarioService

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})

def crear_usuario(request):
    trabajadores = Trabajador.objects.all()  # Obtener todos los trabajadores
    roles = Rol.objects.all()  # Obtener todos los roles
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuario')
        trabajador_id = request.POST.get('trabajador')  # Asignar el trabajador
        rol_id = request.POST.get('rol')  # Asignar el rol
        contrasena = request.POST.get('contrasena')
        UsuarioService.crear_usuario(nombre_usuario, trabajador_id, rol_id, contrasena)
        return redirect('lista_usuarios')
    return render(request, 'usuarios/formulario.html', {'roles': roles, 'trabajadores': trabajadores})

def actualizar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, pk=id_usuario)
    trabajadores = Trabajador.objects.all()  # Obtener todos los trabajadores
    roles = Rol.objects.all()  # Obtener todos los roles
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuario')
        trabajador_id = request.POST.get('trabajador')
        rol_id = request.POST.get('rol')
        contrasena = request.POST.get('contrasena')

        UsuarioService.actualizar_usuario(id_usuario, nombre_usuario, trabajador_id, rol_id, contrasena)
        
        return redirect('lista_usuarios')
    return render(request, 'usuarios/formulario.html', {'usuario': usuario, 'roles': roles, 'trabajadores': trabajadores})

def eliminar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, pk=id_usuario)  # Obtener el usuario o mostrar un 404 si no existe

    if request.method == 'POST':
        UsuarioService.eliminar_usuario(id_usuario)  # Llamar al servicio para eliminar el usuario
        return redirect('lista_usuarios')  # Redirigir a la lista después de eliminar

    # Si el método es GET, mostramos una página de confirmación
    return render(request, 'usuarios/eliminar.html', {'usuario': usuario})
