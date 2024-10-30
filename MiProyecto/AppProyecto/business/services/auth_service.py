from AppProyecto.data.repositories.user_repository import UserRepository

class AuthService:
    @staticmethod
    def login(nombre_usuario, contrasena):
        usuario = UserRepository.get_user_by_username(nombre_usuario)
        if usuario and UserRepository.validate_password(usuario, contrasena):
            return usuario
        return None