from django.test import TestCase
from AppProyecto.models import Trabajador, Genero

class TrabajadorModelTest(TestCase):
    def setUp(self):
        """Configura los objetos necesarios para las pruebas."""
        self.genero = Genero.objects.create(nombre="Masculino")
        self.trabajador = Trabajador.objects.create(
            rut="20.614.309-6",
            nombre="Bastian Pavez",
            genero=self.genero,
            direccion="Benozzo Gozzoli 6028",
            telefono="995749451"
        )

    def test_trabajador_nombre(self):
        self.assertEqual(self.trabajador.nombre, "Bastian Pavez")