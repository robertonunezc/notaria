from django import forms
from notaria.main.models import Persona, Ocupacion, TipoIdentificacion, DatosBasicos#, Direccion, Pais, NEstado
from django.contrib.admin import widgets

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        exclude = ('user',)


class OcupacionForm(forms.ModelForm):
    class Meta:
        model = Ocupacion
        fields = '__all__'

#
# class PaisNacimientoForm(forms.ModelForm):
#     class Meta:
#         model = Pais
#         fields = '__all__'

# class PaisOrigenForm(forms.ModelForm):
#     class Meta:
#         model = Pais
#         fields = '__all__'

class TipoIdentificacionForm(forms.ModelForm):
    class Meta:
        model = TipoIdentificacion
        fields = '__all__'


# class DireccionForm(forms.ModelForm):
#     estado = forms.ModelChoiceField(queryset=NEstado.objects.filter(activo=True), empty_label='--selecciona--',
#                                     label='Estado',
#                                     required=False)
#     class Meta:
#         model = Direccion
#         fields = '__all__'


class DatosBasicosForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'class': 'date-picker'}))
    fecha_matrimonio = forms.DateField(widget=forms.DateInput(attrs={'class': 'date-picker'}))
    class Meta:
        model = DatosBasicos
        fields = '__all__'
