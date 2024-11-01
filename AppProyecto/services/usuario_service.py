from AppProyecto.repositories.usuario_repository import UsuarioRepository
from django.contrib.auth.hashers import make_password
from AppProyecto.models import Usuario

class UsuarioService:

    @staticmethod
    def crear_usuario(datos):
        datos['contrasena'] = make_password(datos['contrasena'])
        usuario = Usuario(**datos)
        UsuarioRepository.guardar(usuario)
        return usuario

    @staticmethod
    def actualizar_usuario(usuario, datos):
        if 'contrasena' in datos and datos['contrasena']:
            datos['contrasena'] = make_password(datos['contrasena'])
        for campo, valor in datos.items():
            setattr(usuario, campo, valor)
        UsuarioRepository.guardar(usuario)

    @staticmethod
    def eliminar_usuario(usuario):
        UsuarioRepository.eliminar(usuario)

