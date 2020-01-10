from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from notaria.main.models import DatosBasicos
from notaria.datos_basicos.forms import DatosBasicosForm

def alta_datos_basicos(request):
    form = DatosBasicosForm()
    if request.method == 'POST':
        form = DatosBasicosForm(request.POST, request.FILES)
        if form.is_valid():
            return redirect('datos_basicos:listado_expedientes')
    context = {
        'form': form
    }
    return render(request, 'datos_basicos/alta_datos_basicos.html', context=context)