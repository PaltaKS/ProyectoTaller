# AppProyecto/views/usuario_views.py
from django.shortcuts import render, redirect, get_object_or_404
from AppProyecto.services.usuario_service import UsuarioService
from AppProyecto.models import Trabajador, Rol

# Listar Usuarios
def listar_usuarios(request):
    usuarios = UsuarioService.listar_usuarios()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})

# Crear Usuario
def crear_usuario(request):
    trabajadores = Trabajador.objects.all()
    roles = Rol.objects.all()
    if request.method == 'POST':
        datos = {
            'nombre_usuario': request.POST.get('nombre_usuario'),
            'trabajador_id': request.POST.get('trabajador'),
            'rol_id': request.POST.get('rol'),
            'contrasena': request.POST.get('contrasena'),
        }
        UsuarioService.crear_usuario(datos)
        return redirect('lista_usuarios')
    return render(request, 'usuarios/formulario.html', {'trabajadores': trabajadores, 'roles': roles})

# Actualizar Usuario
def actualizar_usuario(request, id_usuario):
    usuario = UsuarioService.obtener_usuario_por_id(id_usuario)
    trabajadores = Trabajador.objects.all()
    roles = Rol.objects.all()
    if request.method == 'POST':
        datos = {
            'nombre_usuario': request.POST.get('nombre_usuario'),
            'trabajador_id': request.POST.get('trabajador'),
            'rol_id': request.POST.get('rol'),
            'contrasena': request.POST.get('contrasena'),
        }
        UsuarioService.actualizar_usuario(usuario, datos)
        return redirect('lista_usuarios')
    return render(request, 'usuarios/formulario.html', {'usuario': usuario, 'trabajadores': trabajadores, 'roles': roles})

# Eliminar Usuario
def eliminar_usuario(request, id_usuario):
    usuario = UsuarioService.obtener_usuario_por_id(id_usuario)
    if request.method == 'POST':
        UsuarioService.eliminar_usuario(usuario)
        return redirect('lista_usuarios')
    return render(request, 'usuarios/eliminar.html', {'usuario': usuario})
