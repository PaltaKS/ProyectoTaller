from django.shortcuts import render, redirect, get_object_or_404
from AppProyecto.services.datos_laborales_services import DatosLaboralesService
from AppProyecto.models import Trabajador

def lista_datos_laborales(request):
    datos_laborales = DatosLaboralesService.listar_todos()
    return render(request, 'DatosLaborales/lista.html', {'datos_laborales': datos_laborales})

def crear_datos_laborales(request):
    if request.method == 'POST':
        datos_laborales_data = {
            'trabajador_id': request.POST['trabajador'],
            'cargo': request.POST['cargo'],
            'fecha_ingreso': request.POST['fecha_ingreso'],
            'area': request.POST['area'],
            'departamento': request.POST['departamento']
        }
        DatosLaboralesService.crear(datos_laborales_data)
        return redirect('lista_datos_laborales')
    
    trabajadores = Trabajador.objects.all()
    return render(request, 'DatosLaborales/formulario.html', {'trabajadores': trabajadores})

def editar_datos_laborales(request, id_datos_laborales):
    datos_laborales = DatosLaboralesService.obtener_por_id(id_datos_laborales)
    if request.method == 'POST':
        datos_laborales_data = {
            'trabajador_id': request.POST['trabajador'],
            'cargo': request.POST['cargo'],
            'fecha_ingreso': request.POST['fecha_ingreso'],
            'area': request.POST['area'],
            'departamento': request.POST['departamento']
        }
        DatosLaboralesService.actualizar(id_datos_laborales, datos_laborales_data)
        return redirect('lista_datos_laborales')
    
    trabajadores = Trabajador.objects.all()
    return render(request, 'DatosLaborales/formulario.html', {'datos_laborales': datos_laborales, 'trabajadores': trabajadores})

def eliminar_datos_laborales(request, id_datos_laborales):
    datos_laborales = DatosLaboralesService.obtener_por_id(id_datos_laborales)
    if request.method == 'POST':
        # Realiza la eliminación
        DatosLaboralesService.eliminar(id_datos_laborales)
        return redirect('lista_datos_laborales')
    
    # Renderiza la página de confirmación si el método es GET
    return render(request, 'DatosLaborales/eliminar.html', {'datos_laborales': datos_laborales})
