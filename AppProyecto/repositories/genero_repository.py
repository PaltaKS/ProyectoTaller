from AppProyecto.models import Genero

class GeneroRepository:

    @staticmethod
    def obtener_todos():
        return Genero.objects.all()

    @staticmethod
    def obtener_por_id(id_genero):
        return Genero.objects.filter(id_genero=id_genero).first()

    @staticmethod
    def crear_genero(data):
        genero = Genero(**data)
        genero.save()
        return genero

    @staticmethod
    def actualizar_genero(id_genero, data):
        genero = GeneroRepository.obtener_por_id(id_genero)
        if genero:
            for key, value in data.items():
                setattr(genero, key, value)
            genero.save()
        return genero

    @staticmethod
    def eliminar_genero(id_genero):
        genero = GeneroRepository.obtener_por_id(id_genero)
        if genero:
            genero.delete()
