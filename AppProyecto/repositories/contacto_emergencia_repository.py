from AppProyecto.models import ContactoEmergencia

class ContactoEmergenciaRepository:
    @staticmethod
    def listar_contactos():
        return ContactoEmergencia.objects.all()

    @staticmethod
    def obtener_contacto(contacto_id):
        try:
            return ContactoEmergencia.objects.get(id_contacto=contacto_id)
        except ContactoEmergencia.DoesNotExist:
            return None

    @staticmethod
    def crear_contacto(data):
        return ContactoEmergencia.objects.create(**data)

    @staticmethod
    def actualizar_contacto(contacto_id, data):
        contacto = ContactoEmergenciaRepository.obtener_contacto(contacto_id)
        if contacto:
            for key, value in data.items():
                setattr(contacto, key, value)
            contacto.save()
            return contacto
        return None

    @staticmethod
    def eliminar_contacto(contacto_id):
        contacto = ContactoEmergenciaRepository.obtener_contacto(contacto_id)
        if contacto:
            contacto.delete()
            return True
        return False
