from AppProyecto.models import Trabajador

class TrabajadorRepository:
    def create(self, data):
        trabajador = Trabajador(**data)
        trabajador.save()
        return trabajador

    def get_all(self):
        return Trabajador.objects.all()

    def get_by_id(self, trabajador_id):
        return Trabajador.objects.get(id_trabajador=trabajador_id)

    def update(self, trabajador_id, data):
        trabajador = self.get_by_id(trabajador_id)
        for attr, value in data.items():
            setattr(trabajador, attr, value)
        trabajador.save()
        return trabajador

    def delete(self, trabajador_id):
        trabajador = self.get_by_id(trabajador_id)
        trabajador.delete()
        return trabajador