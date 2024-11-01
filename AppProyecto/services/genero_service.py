from AppProyecto.repositories.genero_repository import GeneroRepository

class GeneroService:

    @staticmethod
    def listar_generos():
        return GeneroRepository.obtener_todos()

    @staticmethod
    def obtener_genero(id_genero):
        return GeneroRepository.obtener_por_id(id_genero)

    @staticmethod
    def crear_genero(data):
        return GeneroRepository.crear_genero(data)

    @staticmethod
    def actualizar_genero(id_genero, data):
        return GeneroRepository.actualizar_genero(id_genero, data)

    @staticmethod
    def eliminar_genero(id_genero):
        return GeneroRepository.eliminar_genero(id_genero)
