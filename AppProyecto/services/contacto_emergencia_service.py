from AppProyecto.repositories.contacto_emergencia_repository import ContactoEmergenciaRepository

class ContactoEmergenciaService:
    @staticmethod
    def listar_contactos():
        return ContactoEmergenciaRepository.listar_contactos()

    @staticmethod
    def obtener_contacto(contacto_id):
        return ContactoEmergenciaRepository.obtener_contacto(contacto_id)

    @staticmethod
    def crear_contacto(data):
        # Aquí podrías agregar validaciones adicionales si es necesario
        return ContactoEmergenciaRepository.crear_contacto(data)

    @staticmethod
    def actualizar_contacto(contacto_id, data):
        return ContactoEmergenciaRepository.actualizar_contacto(contacto_id, data)

    @staticmethod
    def eliminar_contacto(contacto_id):
        return ContactoEmergenciaRepository.eliminar_contacto(contacto_id)
