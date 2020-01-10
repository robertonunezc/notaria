from django import forms
from notaria.main.models import Persona, ConyugeActual, Ocupacion, Pais, TipoIdentificacion, DatosBasicos, NEstado, Direccion


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        exclude = ('user',)

class ConyugeActualForm(forms.ModelForm):
    class Meta:
        model = ConyugeActual
        exclude = ('user',)

class OcupacionForm(forms.ModelForm):
    class Meta:
        model = Ocupacion
        fields = '__all__'


class PaisNacimientoForm(forms.ModelForm):
    CHOICES = [[x.id, x.nombre] for x in Pais.objects.all()]

    pais_nacimiento = forms.MultipleChoiceField(choices=CHOICES, required=True, widget=forms.Select)

    class Meta:
        model = Pais
        fields = '__all__'

class PaisOrigenForm(forms.ModelForm):
    CHOICES = [[x.id, x.nombre] for x in Pais.objects.all()]

    pais_origen = forms.MultipleChoiceField(choices=CHOICES, required=True, widget=forms.Select)

    class Meta:
        model = Pais
        fields = '__all__'

class TipoIdentificacionForm(forms.ModelForm):
    CHOICES = [[x.id, x.nombre] for x in TipoIdentificacion.objects.all()]

    pais_origen = forms.MultipleChoiceField(choices=CHOICES, required=True, widget=forms.Select)

    class Meta:
        model = TipoIdentificacion
        fields = '__all__'


class DireccionForm(forms.ModelForm):
    estado = forms.ModelChoiceField(queryset=NEstado.objects.filter(activo=True), empty_label='--selecciona--',
                                    label='Estado',
                                    required=False)

    class Meta:
        model = Direccion
        fields = '__all__'


class DatosBasicosForm(forms.ModelForm):
    class Meta:
        model = DatosBasicos
        fields = '__all__'
