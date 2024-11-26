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
        Crea un trabajador si el RUT no está registrado y los datos son válidos.
        """
        # Validación de campos requeridos
        campos_requeridos = ['rut', 'nombre', 'genero_id', 'direccion', 'telefono']
        for campo in campos_requeridos:
            if not data.get(campo):
                raise ValueError(f"El campo {campo} es obligatorio.")

        # Validación específica del RUT
        trabajador_existente = TrabajadorRepository.obtener_por_rut(data['rut'])
        if trabajador_existente:
            raise ValueError(f"El RUT {data['rut']} ya está asignado a un trabajador existente.")

        # Validaciones de longitud
        if len(data['nombre']) > 100:
            raise ValueError("El nombre no puede exceder los 100 caracteres")
        if len(data['direccion']) > 200:
            raise ValueError("La dirección no puede exceder los 200 caracteres")

        # Si pasa todas las validaciones, crear el trabajador
        trabajador = TrabajadorRepository.create_trabajador(data)
        return trabajador

    @staticmethod
    def actualizar_trabajador(rut, data):
        return TrabajadorRepository.actualizar_trabajador(rut, data)

    @staticmethod
    def eliminar_trabajador(rut):
        return TrabajadorRepository.eliminar_trabajador(rut)
