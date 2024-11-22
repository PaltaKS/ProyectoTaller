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
    def create_trabajador(data):

        trabajador = Trabajador.objects.create(**data)
        return trabajador

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
