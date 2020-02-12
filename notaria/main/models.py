from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.core.validators import RegexValidator

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
        full_name = '%s %s %s' % (self.nombre, self.apellido_paterno, self.apellido_materno)
        return full_name.strip()

    def __str__(self):
        return self.get_full_name().strip()


class Ocupacion(models.Model):
    class Meta:
        verbose_name = 'Ocupación'
        verbose_name_plural = "Ocupaciones"
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

# class Pais(models.Model):
#     nombre = models.CharField(max_length=80)
#     def __str__(self):
#         return self.nombre


class TipoIdentificacion(models.Model):
    class Meta:
        verbose_name = 'Tipo de Identificación'
        verbose_name_plural = "Tipos de Identificación"
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre


class TipoTramite(models.Model):
    class Meta:
        verbose_name = 'Tipo de trámite'
        verbose_name_plural = "Tipos de trámites"
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class DatosBasicos(Persona):
    tipo_de_tramite = models.ForeignKey(TipoTramite, on_delete=models.SET_NULL, null=True)
    #usuario = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    SR = 0
    SRA = 1
    TITULOPERSONAL = (
        (SR, "Sr"),
        (SRA, "Sra")
    )

    MASCULINO = 0
    FEMENINO = 1
    GENERO = (
        (MASCULINO, "Masculino"),
        (FEMENINO, "Femenino")
    )

    CASADO_BIENES_MANCOMUNADOS = 0
    CASADO_BIENES_SEPARADOS = 4
    SOLTERO = 1
    DIVORCIADO = 2
    VIUDO = 3

    ESTADOCIVIL = (
        (CASADO_BIENES_MANCOMUNADOS, "Casado Bienes Mancomunados"),
        (CASADO_BIENES_SEPARADOS, "Casado Bienes Separados"),
        (SOLTERO, "Soltero"),
        (DIVORCIADO, "Divorciado"),
        (VIUDO, "Viudo")
    )

    titulo = models.IntegerField(choices=TITULOPERSONAL)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    sexo = models.IntegerField(choices=GENERO)
    ocupacion = models.ForeignKey(Ocupacion, on_delete=models.SET_NULL, null=True)
    pais_nacimiento = models.CharField(max_length=80) #models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, related_name='natural')
    pais_nacionalidad = models.CharField(max_length=80) #models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, related_name='nacionalidad')
    ciudad_de_origen = models.CharField(max_length=80)
    documento_migratorio = models.CharField(max_length=80, null=True, blank=True)
    calidad_migratoria = models.CharField(max_length=80, blank=True, null=True)
    tipo_de_identificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.SET_NULL, null=True)
    folio_de_identificacion = models.CharField(max_length=80, null=True, blank=True)
    emite_identificacion = models.CharField(max_length=80, null=True, blank=True)
    clave_larga_distancia = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], blank=True, null=True)
    telefono_casa = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], blank=True, null=True)
    telefono_casa_2 = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], blank=True, null=True)
    extension = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], blank=True, null=True)
    celular = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    celular_2 = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], blank=True, null=True)
    telefono_oficina = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], blank=True, null=True)
    telefono_oficina_2 = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], blank=True, null=True)
    email = models.CharField(max_length=80)
    email_2 = models.CharField(max_length=80, blank=True, null=True)
    email_3 = models.CharField(max_length=80, blank=True, null=True)
    facebook = models.CharField(max_length=80, blank=True, null=True)
    twitter = models.CharField(max_length=80, blank=True, null=True)
    web = models.CharField(max_length=80, blank=True, null=True)
    estado_civil = models.IntegerField(choices=ESTADOCIVIL)
    conyuge_apellido_paterno = models.CharField(max_length=80, blank=True, null=True)
    conyuge_apellido_materno = models.CharField(max_length=80, blank=True, null=True)
    conyuge_nombre = models.CharField(max_length=80, blank=True, null=True)
    fecha_matrimonio = models.DateField(blank=True, null=True)
    registro_civil = models.CharField(max_length=80, blank=True, null=True)
    nro_acta = models.CharField(max_length=80, blank=True, null=True)
    fecha_creacion = models.DateField(auto_created=True, blank=True, null=True)

    def get_full_name(self):
        full_name = '%s. %s %s %s' % (self.TITULOPERSONAL[self.titulo][1], self.nombre, self.apellido_paterno, self.apellido_materno)
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
    class Meta:
        verbose_name = 'Código Postal'
        verbose_name_plural = "Códigos Postales"
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
