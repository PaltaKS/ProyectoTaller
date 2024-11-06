from AppProyecto.repositories.usuario_repository import UsuarioRepository
from django.contrib.auth.hashers import make_password
from AppProyecto.models import Usuario

class UsuarioService:

    @staticmethod
    def listar_usuarios():
        return UsuarioRepository.listar()

    @staticmethod
    def obtener_usuario_por_id(id_usuario):
        return UsuarioRepository.obtener_por_id(id_usuario)

    @staticmethod
    def crear_usuario(datos):
        datos['contrasena'] = make_password(datos['contrasena'])
        usuario = Usuario(**datos)
        UsuarioRepository.crear(usuario)
        return usuario

    @staticmethod
    def actualizar_usuario(usuario, datos):
        if 'contrasena' in datos and datos['contrasena']:
            datos['contrasena'] = make_password(datos['contrasena'])
        for campo, valor in datos.items():
            setattr(usuario, campo, valor)
        UsuarioRepository.actualizar(usuario)

    @staticmethod
    def eliminar_usuario(usuario):
        UsuarioRepository.eliminar(usuario)
