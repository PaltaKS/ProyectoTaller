# mi_app/repositories.py

from AppProyecto.models import Trabajador

class TrabajadorRepository:

    @staticmethod
    def obtener_todos():
        return Trabajador.objects.all()

    @staticmethod
    def obtener_por_rut(rut):
        return Trabajador.objects.filter(rut=rut).first()

    @staticmethod
    def crear_trabajador(rut, nombre, genero_id, direccion, telefono):
        # Crear y guardar el trabajador
        nuevo_trabajador = Trabajador(
            rut=rut,
            nombre=nombre,
            genero_id=genero_id,  # Asignar el género
            direccion=direccion,
            telefono=telefono
        )
        nuevo_trabajador.save()
        return nuevo_trabajador

    @staticmethod
    def actualizar_trabajador(rut, data):
        trabajador = TrabajadorRepository.obtener_por_rut(rut)
        if trabajador:
            for key, value in data.items():
                setattr(trabajador, key, value)
            trabajador.save()
        return trabajador

    @staticmethod
    def eliminar_trabajador(rut):
        trabajador = TrabajadorRepository.obtener_por_rut(rut)
        if trabajador:
            trabajador.delete()
