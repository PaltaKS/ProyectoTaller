from AppProyecto.models import DatosLaborales

class DatosLaboralesRepository:
    @staticmethod
    def get_all():
        return DatosLaborales.objects.all()

    @staticmethod
    def get_by_id(id_datos_laborales):
        return DatosLaborales.objects.filter(id_datos_laborales=id_datos_laborales).first()

    @staticmethod
    def create(datos_laborales_data):
        datos_laborales = DatosLaborales(**datos_laborales_data)
        datos_laborales.save()
        return datos_laborales

    @staticmethod
    def update(id_datos_laborales, datos_laborales_data):
        DatosLaborales.objects.filter(id_datos_laborales=id_datos_laborales).update(**datos_laborales_data)

    @staticmethod
    def delete(id_datos_laborales):
        DatosLaborales.objects.filter(id_datos_laborales=id_datos_laborales).delete()
