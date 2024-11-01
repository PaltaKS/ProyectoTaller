# AppProyecto/views/genero_views.py

from django.shortcuts import render, redirect
from AppProyecto.services.genero_service import GeneroService
from AppProyecto.forms.forms import GeneroForm  # Asegúrate de crear este formulario

def listar_generos(request):
    generos = GeneroService.listar_generos()
    return render(request, 'genero/lista.html', {'generos': generos})

def crear_genero(request):
    if request.method == 'POST':
        data = {
            'nombre': request.POST['nombre'],
        }
        GeneroService.crear_genero(data)
        return redirect('lista_generos')
    return render(request, 'genero/formulario.html')

def actualizar_genero(request, id_genero):
    genero = GeneroService.obtener_genero(id_genero)
    if request.method == 'POST':
        data = {
            'nombre': request.POST['nombre'],
        }
        GeneroService.actualizar_genero(id_genero, data)
        return redirect('lista_generos')
    return render(request, 'genero/formulario.html', {'genero': genero})

def eliminar_genero(request, id_genero):
    genero = GeneroService.obtener_genero(id_genero)
    if request.method == 'POST':
        GeneroService.eliminar_genero(id_genero)
        return redirect('lista_generos')
    return render(request, 'genero/eliminar.html', {'genero': genero})