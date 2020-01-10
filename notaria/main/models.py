from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
# Create your models here.

class User(AbstractUser):
    objects = UserManager()
    def __str__(self):
        return self.username


class Persona(models.Model):
    apellido_paterno = models.CharField(max_length=80)
    apellido_materno = models.CharField(max_length=80)
    nombre = models.CharField(max_length=80)

    def get_full_name(self):
        full_name = '%s %s %s' % (self.nombre, self.primer_apellido, self.segundo_apellido)
        return full_name.strip()

    def __str__(self):
        return self.get_full_name().strip()

class ConyugeActual(Persona):
    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_matrimonio = models.DateField(null=False, blank=False)
    registro_civil = models.CharField(max_length=80, unique=True)
    nro_acta = models.CharField(max_length=80, unique=True)

    def get_full_name(self):
        full_name = '%s %s %s' % (self.nombre, self.primer_apellido, self.segundo_apellido)
        return full_name.strip()

    def __str__(self):
        return self.get_full_name().strip()

class Ocupacion(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class Pais(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class TipoIdentificacion(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class DatosBasicos(Persona):
    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    SR = 0
    SRA = 1
    TITULOPERSONAL = (
        (SR, "Sr"),
        (SRA, "Sra")
    )

    MASCULINO = 0
    FEMENINO = 1
    GENERO = (
        (MASCULINO, "MASCULINO"),
        (FEMENINO, "FEMENINO")
    )

    CASADO = 0
    SOLTERO = 1
    DIVORCIADO = 2
    VIUDO = 3

    ESTADOCIVIL = (
        (CASADO, "CASADO"),
        (SOLTERO, "SOLTERO"),
        (DIVORCIADO, "DIVORCIADO"),
        (VIUDO, "VIUDO")
    )

    titulo = models.IntegerField(choices=TITULOPERSONAL)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    sexo = models.IntegerField(choices=GENERO)
    ocupacion = models.ForeignKey(Ocupacion, on_delete=models.SET_NULL, null=True)
    pais_nacimiento = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, related_name='natural')
    pais_nacionalidad = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, related_name='nacionalidad')
    ciudad_de_origen = models.CharField(max_length=80, unique=True)
    documento_migratorio = models.CharField(max_length=80, unique=True)
    calidad_migratoria = models.CharField(max_length=80, unique=True)
    tipo_de_identificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.SET_NULL, null=True)
    folio_de_identificacion = models.CharField(max_length=80, unique=True)
    emite_identificacion = models.CharField(max_length=80, unique=True)
    clave_larga_distancia = models.IntegerField(unique=True)
    telefono_casa = models.IntegerField(unique=True)
    telefono_casa_2 = models.IntegerField(unique=True)
    extension = models.IntegerField(unique=True)
    celular = models.IntegerField(unique=True)
    celular_2 = models.IntegerField(unique=True)
    telefono_oficina = models.IntegerField(unique=True)
    telefono_oficina_2 = models.IntegerField(unique=True)
    telefono_nextel = models.IntegerField(unique=True)
    id_nextel = models.IntegerField(unique=True)
    email = models.CharField(max_length=80, unique=True)
    email_2 = models.CharField(max_length=80, unique=True)
    email_3 = models.CharField(max_length=80, unique=True)
    facebook = models.CharField(max_length=80, unique=True)
    twitter = models.CharField(max_length=80, unique=True)
    web = models.CharField(max_length=80, unique=True)
    estado_civil = models.IntegerField(choices=ESTADOCIVIL)
    conyuge = models.ForeignKey(ConyugeActual, on_delete=models.SET_NULL, null=True)

    def get_full_name(self):
        full_name = '%s %s %s' % (self.nombre, self.primer_apellido, self.segundo_apellido)
        return full_name.strip()

    def __str__(self):
        return self.get_full_name().strip()

class NEstado(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class NMunicipio(models.Model):
    nombre = models.CharField(max_length=80)
    estado = models.ForeignKey(NEstado, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class NCodigoPostal(models.Model):
    codigo = models.CharField(max_length=80, unique=True)
    municipio = models.ForeignKey(NMunicipio, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.codigo


class NColonia(models.Model):
    nombre = models.CharField(max_length=80)
    codigo_postal = models.ForeignKey(NCodigoPostal, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Direccion(models.Model):
    calle = models.CharField(max_length=250)
    numero_ext = models.CharField(max_length=250)
    numero_int = models.CharField(max_length=250, null=True, blank=True)
    colonia = models.CharField(max_length=250, null=True, blank=True)
    codigo_postal = models.ForeignKey(NColonia, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)
