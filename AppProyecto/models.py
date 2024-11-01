from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.


class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)  # ID de Género
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'
        db_table = 'tbl_generos'

    def __str__(self):
        return self.nombre



class Trabajador(models.Model):
    rut = models.CharField(max_length=20, primary_key=True, unique=True)  # RUT como clave primaria
    nombre = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)  # Relación con Genero
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'
        db_table = 'tbl_trabajadores'

    def __str__(self):
        return self.nombre


class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)  # ID de Rol
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    privilegios = models.ManyToManyField('Privilegio', through='RolPrivilegio', related_name='roles')

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        db_table = 'tbl_roles'

    def __str__(self):
        return self.nombre


class Privilegio(models.Model):
    id_privilegio = models.AutoField(primary_key=True)  # ID de Privilegio
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Privilegio'
        verbose_name_plural = 'Privilegios'
        db_table = 'tbl_privilegios'

    def __str__(self):
        return self.nombre



class RolPrivilegio(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    privilegio = models.ForeignKey(Privilegio, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Rol-Privilegio'
        verbose_name_plural = 'Roles-Privilegios'
        db_table = 'tbl_rol_privilegios'
        unique_together = ('rol', 'privilegio')  # Evitar duplicados

    def __str__(self):
        return f"{self.rol.nombre} - {self.privilegio.nombre}"



class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)  # ID de Usuario
    trabajador = models.OneToOneField(Trabajador, on_delete=models.CASCADE, unique=True)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    nombre_usuario = models.CharField(max_length=50, unique=True)
    contrasena = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'tbl_usuarios'

    def __str__(self):
        return self.nombre_usuario

    def save(self, *args, **kwargs):
        # Hashear la contraseña antes de guardar
        if self.contrasena:  # Solo hasheamos si la contraseña ha sido proporcionada
            self.contrasena = make_password(self.contrasena)
        super(Usuario, self).save(*args, **kwargs)


class ContactoEmergencia(models.Model):
    id_contacto = models.AutoField(primary_key=True)  # ID de Contacto de Emergencia
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    relacion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = 'Contacto de Emergencia'
        verbose_name_plural = 'Contactos de Emergencia'
        db_table = 'tbl_contactosEmergencia'

    def __str__(self):
        return self.nombre


class CargaFamiliar(models.Model):
    id_carga_familiar = models.AutoField(primary_key=True)  # ID de Carga Familiar
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    parentesco = models.CharField(max_length=50, blank=True, null=True)
    genero = models.CharField(max_length=20, blank=True, null=True)
    rut = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = 'Carga Familiar'
        verbose_name_plural = 'Cargas Familiares'
        db_table = 'tbl_cargasFamiliares'

    def __str__(self):
        return self.nombre


class DatosLaborales(models.Model):
    id_datos_laborales = models.AutoField(primary_key=True)  # ID de Datos Laborales
    trabajador = models.OneToOneField(Trabajador, on_delete=models.CASCADE, unique=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Dato Laboral'
        verbose_name_plural = 'Datos Laborales'
        db_table = 'tbl_datosLaborales'

    def __str__(self):
        return f"{self.trabajador.nombre} - {self.cargo}"