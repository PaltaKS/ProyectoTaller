from django.shortcuts import render, redirect
from AppProyecto.services.carga_familiar_services import CargaFamiliarService
from AppProyecto.models import Trabajador, Genero, Parentesco
from django.contrib import messages

def listar_cargas_familiares(request):
    cargas_familiares = CargaFamiliarService.listar_cargas_familiares()
    return render(request, 'CargaFamiliar/lista.html', {'cargas_familiares': cargas_familiares})

def crear_carga_familiar(request):
    parentescos = Parentesco.objects.all()
    generos = Genero.objects.all()
    trabajadores = Trabajador.objects.all()
    
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            parentesco_id = request.POST.get('parentesco')
            genero_id = request.POST.get('genero')
            rut = request.POST.get('rut')
            trabajador_id = request.POST.get('trabajador')
            
            print("Valores recibidos:")
            print(f"Nombre: {nombre}")
            print(f"Parentesco: {parentesco_id}")
            print(f"Género: {genero_id}")
            print(f"RUT: {rut}")
            print(f"Trabajador: {trabajador_id}")

            if  not nombre:
                messages.error(request,'El nombre es requerido')
                return render(request, 'CargaFamiliar/formulario.html', {'values': request.POST, 'parentescos': parentescos, 'generos': generos, 'trabajadores': trabajadores})
            
            if not parentesco_id or parentesco_id == "":
                messages.error(request, 'El parentesco es requerido')
                return render(request, 'CargaFamiliar/formulario.html', {'values': request.POST, 'parentescos': parentescos, 'generos': generos, 'trabajadores': trabajadores})
            
            if not genero_id or genero_id == "":
                messages.error(request, 'El género es requerido')
                return render(request, 'CargaFamiliar/formulario.html', {'values': request.POST, 'parentescos': parentescos, 'generos': generos, 'trabajadores': trabajadores})
            
            if not rut:
                messages.error(request,'El RUT es requerido')
                return render(request, 'CargaFamiliar/formulario.html', {'values': request.POST, 'parentescos': parentescos, 'generos': generos, 'trabajadores': trabajadores})
            
            if not trabajador_id or trabajador_id == "":
                messages.error(request,'Debe seleccionar un trabajador')
                return render(request, 'CargaFamiliar/formulario.html', {'values': request.POST, 'parentescos': parentescos, 'generos': generos, 'trabajadores': trabajadores})
            
            print("Intentando crear carga familiar con:")
            print(f"Trabajador: {trabajador_id}")
            print(f"Nombre: {nombre}")
            print(f"Parentesco: {parentesco_id}")
            print(f"Género: {genero_id}")
            print(f"RUT: {rut}")
            
            CargaFamiliarService.crear_carga(trabajador_id, nombre, parentesco_id, genero_id, rut)
            messages.success(request, 'Carga familiar creada exitosamente')
            return redirect('listar_cargas_familiares')
        
        except Exception as e:
            print(f"Error: {str(e)}")
            messages.error(request, f'Error al crear la carga familiar: {str(e)}')
            return render(request, 'CargaFamiliar/formulario.html', {'values': request.POST, 'parentescos': parentescos, 'generos': generos, 'trabajadores': trabajadores})
    
    return render(request, 'CargaFamiliar/formulario.html', {
        'trabajadores': trabajadores,
        'generos': generos,
        'parentescos': parentescos,
        'values': request.POST
    })
            

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
