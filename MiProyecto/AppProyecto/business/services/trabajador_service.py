from AppProyecto.data.repositories.trabajador_repository import TrabajadorRepository

class TrabajadorService:
    def __init__(self):
        self.trabajador_repository = TrabajadorRepository()

    def create_trabajador(self, data):
        return self.trabajador_repository.create(data)

    def get_all_trabajadores(self):
        return self.trabajador_repository.get_all()

    def get_trabajador(self, trabajador_id):
        return self.trabajador_repository.get_by_id(trabajador_id)

    def update_trabajador(self, trabajador_id, data):
        return self.trabajador_repository.update(trabajador_id, data)

    def delete_trabajador(self, trabajador_id):
        return self.trabajador_repository.delete(trabajador_id)