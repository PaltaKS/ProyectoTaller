from AppProyecto.models import Usuario, Trabajador, Rol
from django.shortcuts import get_object_or_404

class UsuarioRepository:

    @staticmethod
    def listar():
        return Usuario.objects.all()


    @staticmethod
    def obtener_por_id(id_usuario):
        """Obtiene un usuario por su ID."""
        return get_object_or_404(Usuario, id_usuario=id_usuario)


    @staticmethod
    def crear_usuario(nombre_usuario, trabajador, rol, contrasena, email):
        """Crea un nuevo usuario en la base de datos."""
        return Usuario.objects.create(
            nombre_usuario=nombre_usuario,
            trabajador=trabajador,
            rol=rol,
            email=email,
            contrasena=contrasena
        )

        
    @staticmethod
    def actualizar_usuario(usuario):
        """Guarda los cambios en un usuario existente."""
        usuario.save()


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


    ## solo obtenemos datos por id

    @staticmethod   
    def obtener_trabajador_por_id(trabajador_id):
        """Obtiene un trabajador por su ID."""
        return Trabajador.objects.get(id=trabajador_id)
    
    @staticmethod
    def obtener_rol_por_id(rol_id):
        """Obtiene un rol por su ID."""
        return Rol.objects.get(id=rol_id) if rol_id else None
    
    @staticmethod
    def obtener_todos_los_trabajadores():
        """Obtiene todos los trabajadores disponibles."""
        return Trabajador.objects.all()
    
    @staticmethod
    def obtener_todos_los_roles():
        """Obtiene todos los roles disponibles."""
        return Rol.objects.all()
    

    ### Resetear Contrasena

    @staticmethod
    def obtener_por_email(email):
        try:
            return Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return None

    @staticmethod
    def obtener_por_token(token):
        try:
            return Usuario.objects.get(token_recuperacion=token)
        except Usuario.DoesNotExist:
            return None

