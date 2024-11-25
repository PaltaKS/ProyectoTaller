# AppProyecto/views/trabajador_views.py
from AppProyecto.models import Trabajador, Genero
from django.shortcuts import render, redirect, get_object_or_404
from AppProyecto.services.trabajador_service import TrabajadorService
from django.core.paginator import Paginator

def listar_trabajadores(request):
    trabajadores_list = Trabajador.objects.all()  # Obtiene todos los trabajadores
    paginator = Paginator(trabajadores_list, 5)   # Divide en páginas de 5 elementos

    # Obtiene el número de página actual
    page_number = request.GET.get('page')
    trabajadores_page = paginator.get_page(page_number)  # Obtiene la página solicitada

    return render(request, 'trabajadores/lista.html', {'trabajadores': trabajadores_page})

def crear_trabajador(request):
    if request.method == "POST":
        
        # Obtener datos del formulario
        data = {
            "rut": request.POST.get("rut"),
            "nombre": request.POST.get("nombre"),
            "genero_id": request.POST.get("genero"),  # ID de la tabla Genero
            "direccion": request.POST.get("direccion"),
            "telefono": request.POST.get("telefono"),
        }

        # Crear trabajador
        TrabajadorService.crear_trabajador(data)
        return redirect('listar_trabajadores')
        
    # Si no es POST, renderizar formulario vacío
    generos = Genero.objects.all()
    return render(request, "trabajadores/formulario.html", {'generos': generos})

def actualizar_trabajador(request, rut):
    trabajador = get_object_or_404(Trabajador, rut=rut)
    trabajador = TrabajadorService.obtener_trabajador(rut)
    generos = Genero.objects.all()
    if request.method == 'POST':
        data = {
            'nombre': request.POST['nombre'],
            'genero_id': request.POST['genero'],
            'direccion': request.POST.get('direccion', ''),
            'telefono': request.POST.get('telefono', ''),
        }
        TrabajadorService.actualizar_trabajador(rut, data)
        return redirect('listar_trabajadores')
    return render(request, 'trabajadores/formulario.html', {'trabajador': trabajador,'generos': generos})

def eliminar_trabajador(request, rut):
    trabajador = TrabajadorService.obtener_trabajador(rut)
    if request.method == 'POST':
        TrabajadorService.eliminar_trabajador(rut)
        return redirect('listar_trabajadores')
    return render(request, 'trabajadores/eliminar.html', {'trabajador': trabajador})
