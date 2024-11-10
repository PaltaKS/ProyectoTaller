from AppProyecto.repositories.datos_laborales_repository import DatosLaboralesRepository

class DatosLaboralesService:
    @staticmethod
    def listar_todos():
        return DatosLaboralesRepository.get_all()

    @staticmethod
    def obtener_por_id(id_datos_laborales):
        return DatosLaboralesRepository.get_by_id(id_datos_laborales)

    @staticmethod
    def crear(datos_laborales_data):
        return DatosLaboralesRepository.create(datos_laborales_data)

    @staticmethod
    def actualizar(id_datos_laborales, datos_laborales_data):
        DatosLaboralesRepository.update(id_datos_laborales, datos_laborales_data)

    @staticmethod
    def eliminar(id_datos_laborales):
        DatosLaboralesRepository.delete(id_datos_laborales)
