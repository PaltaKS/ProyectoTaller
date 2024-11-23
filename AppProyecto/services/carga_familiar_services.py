from AppProyecto.repositories.carga_familiar_repositories import CargaFamiliarRepository
from AppProyecto.models import Trabajador, Parentesco

class CargaFamiliarService:

    @staticmethod
    def listar_cargas_familiares():
        return CargaFamiliarRepository.listar()

    @staticmethod
    def obtener_carga_por_id(carga_id):
        return CargaFamiliarRepository.obtener_por_id(carga_id)

    @staticmethod
    def crear_carga(trabajador_id, nombre, parentesco_id, genero_id, rut):
        trabajador = Trabajador.objects.get(rut=trabajador_id)
        parentesco = Parentesco.objects.get(pk=parentesco_id)




        return CargaFamiliarRepository.crear(trabajador, nombre, parentesco, genero_id, rut)

    @staticmethod
    def actualizar_carga(carga_id, nombre, parentesco, genero, rut, trabajador_id):
        carga = CargaFamiliarRepository.obtener_por_id(carga_id)
        trabajador = Trabajador.objects.get(rut=trabajador_id)
        return CargaFamiliarRepository.actualizar(carga, nombre, parentesco, genero, rut, trabajador)

    @staticmethod
    def eliminar_carga(carga_id):
        carga = CargaFamiliarRepository.obtener_por_id(carga_id)
        CargaFamiliarRepository.eliminar(carga)
