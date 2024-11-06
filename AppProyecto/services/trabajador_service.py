from AppProyecto.repositories.trabajador_repository import TrabajadorRepository

class TrabajadorService:

    @staticmethod
    def listar_trabajadores():
        return TrabajadorRepository.obtener_todos()

    @staticmethod
    def obtener_trabajador(rut):
        return TrabajadorRepository.obtener_por_rut(rut)

    @staticmethod
    def crear_trabajador(rut, nombre, genero_id, direccion, telefono):
        return TrabajadorRepository.crear_trabajador(rut, nombre, genero_id, direccion, telefono)

    @staticmethod
    def actualizar_trabajador(rut, data):
        return TrabajadorRepository.actualizar_trabajador(rut, data)

    @staticmethod
    def eliminar_trabajador(rut):
        return TrabajadorRepository.eliminar_trabajador(rut)
