from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from notaria.main.models import DatosBasicos
from notaria.datos_basicos.forms import DatosBasicosForm
from django.contrib.auth.decorators import login_required


def alta_datos_basicos(request):
    form = DatosBasicosForm()
    if request.method == 'POST':
        form = DatosBasicosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('datos_basicos:listado_datos_basicos')
    context = {
        'form': form
    }
    return render(request, 'datos_basicos/alta_datos_basicos.html', context=context)

@login_required
def listado_datos_basicos(request):
    datos_basicos = DatosBasicos.objects.all().order_by('-id')
    context = {
        'datos_basicos': datos_basicos
    }
    return render(request, 'datos_basicos/listado_datos_basicos.html', context=context)

@login_required
def editar_datos_basicos(request, datos_basicos_id):
    datos_basicos = DatosBasicos.objects.get(pk=datos_basicos_id)
    form = DatosBasicosForm(instance=datos_basicos)
    if request.method == 'POST':
        form = DatosBasicosForm(request.POST, instance=datos_basicos)
        if form.is_valid():
            form.save()
            return redirect('datos_basicos:listado_datos_basicos')
    context = {
        'form': form
    }
    return render(request, 'datos_basicos/editar_datos_basicos.html', context=context)