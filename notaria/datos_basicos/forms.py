from django import forms
from notaria.main.models import Persona, Ocupacion, Pais, TipoIdentificacion, DatosBasicos, NEstado, Direccion


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        exclude = ('user',)


class OcupacionForm(forms.ModelForm):
    class Meta:
        model = Ocupacion
        fields = '__all__'


class PaisNacimientoForm(forms.ModelForm):
    query_set = Pais.objects.all()

    pais_nacimiento = forms.MultipleChoiceField(choices=query_set, required=True, widget=forms.Select)

    class Meta:
        model = Pais
        fields = '__all__'

class PaisOrigenForm(forms.ModelForm):
    query_set = Pais.objects.all()

    pais_origen = forms.MultipleChoiceField(choices=query_set, required=True, widget=forms.Select)

    class Meta:
        model = Pais
        fields = '__all__'

class TipoIdentificacionForm(forms.ModelForm):

    query_set = TipoIdentificacion.objects.all()
    pais_origen = forms.MultipleChoiceField(choices=query_set, required=True, widget=forms.Select)

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
