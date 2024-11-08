from AppProyecto.repositories.usuario_repository import UsuarioRepository


class UsuarioService:

    @staticmethod
    def listar_usuario():
        return UsuarioRepository.obtener_todos()


    @staticmethod
    def obtener_usuario(id_usuario):
        return UsuarioRepository.obtener_por_id(id_usuario)


    @staticmethod
    def crear_usuario(nombre_usuario, trabajador_id, rol_id, contrasena):
        return UsuarioRepository.crear_usuario(nombre_usuario, trabajador_id, rol_id, contrasena)


    @staticmethod
    def actualizar_usuario(usuario_id, nombre_usuario, trabajador_id, rol_id, contrasena=None):
        return UsuarioRepository.actualizar_usuario(usuario_id, nombre_usuario, trabajador_id, rol_id, contrasena)


    @staticmethod
    def eliminar_usuario(usuario_id):
        return UsuarioRepository.eliminar_usuario(usuario_id)
