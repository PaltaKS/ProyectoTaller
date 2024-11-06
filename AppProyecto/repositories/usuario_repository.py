from AppProyecto.models import Usuario
from django.shortcuts import get_object_or_404

class UsuarioRepository:

    @staticmethod
    def listar():
        return Usuario.objects.all()

    @staticmethod
    def obtener_por_id(id_usuario):
        return get_object_or_404(Usuario, id_usuario=id_usuario)

    @staticmethod
    def crear(usuario):
        usuario.save()

    @staticmethod
    def actualizar(usuario):
        usuario.save()

    @staticmethod
    def eliminar(usuario):
        usuario.delete()
