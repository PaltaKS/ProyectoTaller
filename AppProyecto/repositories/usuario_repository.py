from AppProyecto.models import Usuario

class UsuarioRepository:

    @staticmethod
    def obtener_todos():
        return Usuario.objects.all()

    @staticmethod
    def obtener_por_id(id_usuario):
        return Usuario.objects.get(id_usuario=id_usuario)

    @staticmethod
    def guardar(usuario):
        usuario.save()

    @staticmethod
    def eliminar(usuario):
        usuario.delete()


class UsuarioRepository:
    @staticmethod
    def get_user_by_username(nombre_usuario):
        try:
            return Usuario.objects.get(nombre_usuario=nombre_usuario)
        except Usuario.DoesNotExist:
            return None  # Retorna None si no se encuentra el usuario 
