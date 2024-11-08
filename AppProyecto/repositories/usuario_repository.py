from AppProyecto.models import Usuario, Trabajador, Rol
from django.contrib.auth.hashers import make_password

class UsuarioRepository:

    @staticmethod
    def obtener_todos():
        return Usuario.objects.all()

    @staticmethod
    def obtener_por_id(id_usuario):
        return Usuario.objects.get(id_usuario=id_usuario)


    @staticmethod
    def crear_usuario(nombre_usuario, trabajador_id, rol_id, contrasena):

        obtener_trabajador = Trabajador.objects.get(pk=trabajador_id)
        obtener_rol = Rol.objects.get(pk=rol_id)

        nuevo_usuario = Usuario(
           trabajador = obtener_trabajador,   #asigna el trabajador
           rol = obtener_rol,     #asigna el rol
           nombre_usuario = nombre_usuario,
           contrasena = contrasena
        )
        nuevo_usuario.save()
        return nuevo_usuario


    def actualizar_usuario(usuario_id, nombre_usuario, trabajador_id, rol_id, contrasena=None):
        try:
            # Obtener la instancia de Usuario a partir del usuario_id
            usuario = Usuario.objects.get(pk=usuario_id)

            # Obtener la instancia de Trabajador y Rol
            trabajador_instance = Trabajador.objects.get(pk=trabajador_id)
            rol_instance = Rol.objects.get(pk=rol_id)

            # Actualizar los campos de Usuario
            usuario.nombre_usuario = nombre_usuario
            usuario.trabajador = trabajador_instance
            usuario.rol = rol_instance

            # Solo actualiza la contraseña si se proporciona una nueva
            if contrasena:
                usuario.contrasena = make_password(contrasena)

            # Guardar cambios en la base de datos
            usuario.save()
            return usuario

        except Usuario.DoesNotExist:
            raise ValueError("El usuario especificado no existe.")
        except Trabajador.DoesNotExist:
            raise ValueError("El trabajador especificado no existe.")
        except Rol.DoesNotExist:
            raise ValueError("El rol especificado no existe.")


    @staticmethod
    def eliminar_usuario(usuario_id):
        try:
            usuario = Usuario.objects.get(pk=usuario_id)
            usuario.delete()  # Eliminar el usuario de la base de datos
            return True
        except Usuario.DoesNotExist:
            raise ValueError("El usuario especificado no existe.")
        

        
    @staticmethod
    def get_user_by_username(nombre_usuario):
        try:
            return Usuario.objects.get(nombre_usuario=nombre_usuario)
        except Usuario.DoesNotExist:
            return None  # Retorna None si no se encuentra el usuario 
