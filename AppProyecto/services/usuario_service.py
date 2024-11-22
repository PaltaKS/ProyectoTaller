from AppProyecto.repositories.usuario_repository import UsuarioRepository
from AppProyecto.models import Rol, Trabajador, Usuario
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.utils.crypto import get_random_string




class UsuarioService:
    
    ### CRUD
    
    @staticmethod
    def listar_usuarios():
        return UsuarioRepository.listar()


    @staticmethod
    def obtener_usuario(id_usuario):
        return UsuarioRepository.obtener_por_id(id_usuario)


    @staticmethod
    def crear_usuario(nombre_usuario, trabajador_id, rol_id, contrasena, email):
        
        # Obtener entidades relacionadas
        trabajador = Trabajador.objects.get(pk=trabajador_id)
        rol = Rol.objects.get(pk=rol_id)
        
        # Llamar al repositorio para crear el usuario
        UsuarioRepository.crear_usuario(
            nombre_usuario=nombre_usuario,
            trabajador=trabajador,
            rol=rol,
            email=email,
            contrasena=contrasena
        )


    @staticmethod
    def actualizar_usuario(id_usuario, nombre_usuario, trabajador_id, rol_id, email, contrasena):
        
        usuario = Usuario.objects.get(pk=id_usuario)
        trabajador_instance = Trabajador.objects.get(pk=trabajador_id)
        rol_instance = Rol.objects.get(pk=rol_id)

        # Actualizar datos del usuario
        usuario.nombre_usuario = nombre_usuario
        usuario.trabajador = trabajador_instance
        usuario.rol = rol_instance
        usuario.email = email
        
        # Actualizar contraseña si se proporciona una nueva
        if contrasena:
            usuario.contrasena = make_password(contrasena)
        
        # Llamar al repositorio para guardar los cambios
        UsuarioRepository.actualizar_usuario(usuario)

    @staticmethod
    def eliminar_usuario(usuario_id):
        return UsuarioRepository.eliminar_usuario(usuario_id)
    

    ### Recuperación de contraseña

    @staticmethod
    def enviar_correo_recuperacion(email):
        usuario = UsuarioRepository.obtener_por_email(email)
        if not usuario:
            return False  # Usuario no encontrado

        # Generar un token único
        token = get_random_string(32)
        usuario.token_recuperacion = token
        UsuarioRepository.actualizar_usuario(usuario)

        # Configura la URL de restablecimiento
        reset_url = f"http://127.0.0.1:8000/restablecer-contrasena/{token}"


        # Configura el correo
        subject = "Recuperación de contraseña"
        message = f"""
        Hola {usuario.nombre_usuario},

        Haz clic en el siguiente enlace para restablecer tu contraseña:
        {reset_url}

        Si no solicitaste este cambio, ignora este mensaje.
        """
        from_email = 'basty.03@hotmail.com'

        # Envía el correo
        try:
            send_mail(subject, message, from_email, [email])
            return True
        except Exception as e:
            print(f"Error al enviar el correo: {e}")  # Verifica los errores en la consola
            return False


    @staticmethod
    def restablecer_contrasena(token, nueva_contrasena):
        usuario = UsuarioRepository.obtener_por_token(token)
        if not usuario:
            return False  # Token inválido
        
        # Hasheamos la nueva contraseña antes de asignarla al usuario
        usuario.contrasena = make_password(nueva_contrasena)
        usuario.token_recuperacion = None  # Invalida el token después de usarlo

        # Usamos el método actualizar_usuario para guardar los cambios
        UsuarioRepository.actualizar_usuario(usuario)  # Esto llamará a save() del modelo

        return True