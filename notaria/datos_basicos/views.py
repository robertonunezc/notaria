from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from notaria.main.models import DatosBasicos
from notaria.datos_basicos.forms import DatosBasicosForm

def alta_datos_basicos(request):
    form = DatosBasicosForm()
    if request.method == 'POST':
        form = DatosBasicosForm(request.POST, request.FILES)
        if form.is_valid():
            return redirect('datos_basicos:listado_datos_basicos')
    context = {
        'form': form
    }
    return render(request, 'datos_basicos/alta_datos_basicos.html', context=context)

def listado_datos_basicos(request):
    datos_basicos = DatosBasicos.objects.all().order_by('-id')
    context = {
        'datos_basicos': datos_basicos
    }
    return render(request, 'datos_basicos/listado_datos_basicos.html', context=context)

