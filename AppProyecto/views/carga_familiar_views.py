from django.shortcuts import render, redirect
from AppProyecto.services.carga_familiar_services import CargaFamiliarService
from AppProyecto.models import Trabajador, Genero, Parentesco

def listar_cargas_familiares(request):
    cargas_familiares = CargaFamiliarService.listar_cargas_familiares()
    return render(request, 'CargaFamiliar/lista.html', {'cargas_familiares': cargas_familiares})

def crear_carga_familiar(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        parentesco = request.POST.get('parentesco')
        genero_id = request.POST.get('genero')
        rut = request.POST.get('rut')
        trabajador_id = request.POST.get('trabajador')
        CargaFamiliarService.crear_carga(trabajador_id, nombre, parentesco, genero_id, rut)
        return redirect('listar_cargas_familiares')
    parentescos = Parentesco.objects.all()
    generos = Genero.objects.all()
    trabajadores = Trabajador.objects.all()
    return render(request, 'CargaFamiliar/formulario.html', {'trabajadores': trabajadores, 'generos': generos, 'parentescos': parentescos})

def editar_carga_familiar(request, carga_id):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        parentesco = request.POST.get('parentesco')
        genero = request.POST.get('genero')
        rut = request.POST.get('rut')
        trabajador_id = request.POST.get('trabajador')
        CargaFamiliarService.actualizar_carga(carga_id, nombre, parentesco, genero, rut, trabajador_id)
        return redirect('listar_cargas_familiares')

    carga_familiar = CargaFamiliarService.obtener_carga_por_id(carga_id)
    trabajadores = Trabajador.objects.all()
    return render(request, 'CargaFamiliar/formulario.html', {
        'carga_familiar': carga_familiar,
        'trabajadores': trabajadores
    })

def eliminar_carga_familiar(request, carga_id):
    if request.method == 'POST':
        CargaFamiliarService.eliminar_carga(carga_id)
        return redirect('listar_cargas_familiares')

    carga_familiar = CargaFamiliarService.obtener_carga_por_id(carga_id)
    return render(request, 'CargaFamiliar/eliminar.html', {'carga_familiar': carga_familiar})
