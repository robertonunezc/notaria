from django.contrib import admin
from notaria.main.models import *
admin.site.site_header = "Administrador notaría"
admin.site.site_title = "Administrador notaría"
admin.site.index_title = "Bienvenidos al portal de administración"
# Register your models here.
admin.site.register(Ocupacion)
admin.site.register(TipoTramite)
#admin.site.register(Pais)
admin.site.register(TipoIdentificacion)
#admin.site.register(NEstado)
#admin.site.register(NMunicipio)
#admin.site.register(NColonia)
admin.site.register(NCodigoPostal)
# Register your models here.

