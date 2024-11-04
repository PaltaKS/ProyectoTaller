# AppProyecto/views/trabajador_views.py
from AppProyecto.models import Trabajador, Genero
from django.shortcuts import render, redirect, get_object_or_404
from AppProyecto.services.trabajador_service import TrabajadorService

def listar_trabajadores(request):
    trabajadores = TrabajadorService.listar_trabajadores()
    return render(request, 'trabajadores/lista.html', {'trabajadores': trabajadores})

def crear_trabajador(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        genero_id = request.POST.get('genero')  # ID del género
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')

        # Crear y guardar el trabajador
        nuevo_trabajador = Trabajador(
            rut=rut,
            nombre=nombre,
            genero_id=genero_id,  # Asignar el género
            direccion=direccion,
            telefono=telefono
        )
        nuevo_trabajador.save()  # Guardar el trabajador
        return redirect('lista_trabajadores')  # Redirigir a la lista de trabajadores

    generos = Genero.objects.all()  # Obtener todos los géneros
    return render(request, 'trabajadores/formulario.html', {'generos': generos})

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
