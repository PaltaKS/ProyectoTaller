from AppProyecto.data.repositories.user_repositories import get_user_by_credentials


def authenticate_user(nombre_usuario, contrasena):
    usuario = get_user_by_credentials(nombre_usuario, contrasena)
    if usuario:
        return usuario
    return None