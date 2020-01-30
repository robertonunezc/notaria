from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from notaria.main.models import DatosBasicos, TipoTramite
from notaria.datos_basicos.forms import DatosBasicosForm
from django.contrib.auth.decorators import login_required
from openpyxl import Workbook

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
    tipo_tramites = TipoTramite.objects.all()
    if request.method == "POST":
        fecha_inicio = request.POST.get('fecha-inicio')
        fecha_fin = request.POST.get('fecha-fin')
        tipo_tramite_pk = request.POST.get('tipo-tramite')
        datos_basicos = filtrar_datos_basicos(fecha_inicio, fecha_fin, tipo_tramite_pk, datos_basicos, tipo_tramites)

    context = {
        'datos_basicos': datos_basicos,
        'tipo_tramites': tipo_tramites
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


def filtrar_datos_basicos(fecha_inicio, fecha_fin, tipo_tramite_pk, datos_basicos, tipo_tramites):

        if fecha_inicio != "" and fecha_fin != "":
            datos_basicos = datos_basicos.filter(fecha_creacion__gt=fecha_inicio, fecha_creacion__lte=fecha_fin)

        if tipo_tramite_pk != "-1":
            tipo_tramite = tipo_tramites.get(pk=tipo_tramite_pk)
            datos_basicos = datos_basicos.filter(tipo_de_tramite=tipo_tramite)

        return datos_basicos

def get_datos_basicos():
    datos_basicos = DatosBasicos.objects.all().order_by('-id')
    return datos_basicos


@login_required
def exportar_excel(request):
    datos_basicos = get_datos_basicos()
    if request.method == "POST":
        tipo_tramites = TipoTramite.objects.all()
        fecha_inicio = request.POST.get('fecha-inicio')
        fecha_fin = request.POST.get('fecha-fin')
        tipo_tramite_pk = request.POST.get('tipo-tramite')
        datos_basicos = filtrar_datos_basicos(fecha_inicio, fecha_fin, tipo_tramite_pk, datos_basicos, tipo_tramites)

    wb = get_reporte_datos_basicos_workbook(datos_basicos=datos_basicos)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="reporte.xls"'
    wb.save(response)
    return response


def get_reporte_datos_basicos_workbook(datos_basicos):
    wb = Workbook()
    ws = wb.active
    titulos = list()
    titulos.append("Nombre")
    titulos.append("Celular")
    titulos.append("Email")
    ws.append(titulos)
    for dato in datos_basicos:
        datos_list = list()
        datos_list.append(dato.__str__())
        datos_list.append(dato.celular.__str__())
        datos_list.append(dato.email.__str__())
        ws.append(datos_list)
    return wb