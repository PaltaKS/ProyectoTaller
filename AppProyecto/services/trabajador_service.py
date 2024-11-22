from AppProyecto.repositories.trabajador_repository import TrabajadorRepository

class TrabajadorService:

    @staticmethod
    def listar_trabajadores():
        return TrabajadorRepository.obtener_todos()

    @staticmethod
    def obtener_trabajador(rut):
        return TrabajadorRepository.obtener_por_rut(rut)

    @staticmethod
    def crear_trabajador(data):
        """
        Crea un trabajador si el RUT no está registrado.
        """
        rut = data.get('rut')
        if not rut:
            raise ValueError("El RUT es obligatorio.")

        # Verificar si ya existe un trabajador con el RUT
        trabajador_existente = TrabajadorRepository.get_trabajador_by_rut(rut)
        if trabajador_existente:
            raise ValueError(f"El RUT {rut} ya está asignado a un trabajador existente.")

        # Crear el trabajador
        trabajador = TrabajadorRepository.create_trabajador(data)
        return trabajador

    @staticmethod
    def actualizar_trabajador(rut, data):
        return TrabajadorRepository.actualizar_trabajador(rut, data)

    @staticmethod
    def eliminar_trabajador(rut):
        return TrabajadorRepository.eliminar_trabajador(rut)
