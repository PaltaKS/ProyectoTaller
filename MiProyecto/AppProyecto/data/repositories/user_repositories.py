from AppProyecto.models import Usuario

def get_user_by_credentials(nombre_usuario, contrasena):
    try:
        # Busca el usuario por nombre de usuario
        usuario = Usuario.objects.get(nombre_usuario=nombre_usuario)
        
        # Compara la contraseña (asegúrate de usar el método adecuado según cómo guardas la contraseña)
        if usuario.contrasena == contrasena:  # Cambia esto si usas hashing para contraseñas
            return usuario
        
        return None
    except Usuario.DoesNotExist:
        return None
