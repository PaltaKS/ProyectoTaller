# presentation/views/trabajador_view.py
from django.shortcuts import render, redirect, get_object_or_404
from AppProyecto.models import Trabajador, Genero
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

# Listar Trabajadores
def trabajador_list(request):
    trabajadores = Trabajador.objects.all()
    return render(request, 'Trabajadores/trabajador_list.html', {'trabajadores': trabajadores})

# Crear Trabajador
@require_http_methods(["GET", "POST"])
def trabajador_create(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        rut = request.POST.get('rut')
        genero_id = request.POST.get('genero')  # Aquí obtienes el ID del género desde el formulario
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        # Asegúrate de que el ID del género esté presente
        if genero_id:
            genero = Genero.objects.get(id_genero=genero_id)  # Obtén el objeto Genero usando el ID
        else:
            genero = None  # O maneja el caso según tu lógica
        # Crear el trabajador
        trabajador = Trabajador(
            nombre=nombre,
            rut=rut,
            genero=genero,
            direccion=direccion,
            telefono=telefono
        )
        trabajador.save()
        return redirect('trabajador_list')  # Redirige a la lista de trabajadores
    generos = Genero.objects.all()  # Obtén todos los géneros para mostrarlos en el formulario
    return render(request, 'Trabajadores/trabajador_create.html', {'generos': generos})

# Editar Trabajador
def trabajador_update(request, id_trabajador):
    trabajador = get_object_or_404(Trabajador, id_trabajador=id_trabajador)

    if request.method == 'POST':
        trabajador.nombre = request.POST.get('nombre')
        trabajador.rut = request.POST.get('rut')
        trabajador.genero_id = request.POST.get('genero')  # Aquí debes asegurarte de que 'genero' se corresponda con el campo id_genero
        trabajador.direccion = request.POST.get('direccion')
        trabajador.telefono = request.POST.get('telefono')
        trabajador.save()
        return redirect('trabajador_list')  # Redirige a la lista de trabajadores

    generos = Genero.objects.all()  # Obtén todos los géneros para mostrarlos en el formulario
    return render(request, 'Trabajadores/trabajador_update.html', {'trabajador': trabajador, 'generos': generos})

# Eliminar Trabajador
@require_http_methods(["GET", "POST"])
def trabajador_delete(request, id_trabajador):
    trabajador = get_object_or_404(Trabajador, id_trabajador=id_trabajador)

    if request.method == "POST":
        trabajador.delete()
        return redirect('trabajador_list')

    return render(request, 'Trabajadores/trabajador_delete.html', {'trabajador': trabajador})
