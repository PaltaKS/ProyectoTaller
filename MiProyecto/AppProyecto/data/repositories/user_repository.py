from django.contrib.auth.hashers import check_password
from AppProyecto.models import Usuario
from django.db import connection

class UserRepository:
    def get_user_by_username(self, username):
        try:
            return Usuario.objects.get(nombre_usuario=username)
        except Usuario.DoesNotExist:
            return None

    @staticmethod
    def validate_password(usuario, contrasena):
        return check_password(contrasena, usuario.contrasena)
    

    def insert_user(self, username, hashed_password, rol_id, trabajador_id):
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO tbl_usuarios (nombre_usuario, contrasena, rol_id, trabajador_id)
                VALUES (%s, %s, %s, %s)
            """, [username, hashed_password, rol_id, trabajador_id])

    
    def get_user_by_username(self, username):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM tbl_usuarios WHERE nombre_usuario = %s
        """, [username])
        row = cursor.fetchone()
        if row:
            return {
                'id_usuario': row[0],
                'nombre_usuario': row[1],
                'contrasena': row[2],
                'rol_id': row[3],
                'trabajador_id': row[4]
            }
        return None
