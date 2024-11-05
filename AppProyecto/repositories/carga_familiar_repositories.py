from AppProyecto.models import CargaFamiliar
from django.shortcuts import get_object_or_404

class CargaFamiliarRepository:

    @staticmethod
    def listar():
        return CargaFamiliar.objects.all()

    @staticmethod
    def obtener_por_id(carga_id):
        return get_object_or_404(CargaFamiliar, id_carga_familiar=carga_id)

    @staticmethod
    def crear(trabajador, nombre, parentesco, genero, rut):
        nueva_carga = CargaFamiliar(
            trabajador=trabajador,
            nombre=nombre,
            parentesco=parentesco,
            genero=genero,
            rut=rut
        )
        nueva_carga.save()
        return nueva_carga

    @staticmethod
    def actualizar(carga, nombre, parentesco, genero, rut, trabajador):
        carga.nombre = nombre
        carga.parentesco = parentesco
        carga.genero = genero
        carga.rut = rut
        carga.trabajador = trabajador
        carga.save()
        return carga

    @staticmethod
    def eliminar(carga):
        carga.delete()
