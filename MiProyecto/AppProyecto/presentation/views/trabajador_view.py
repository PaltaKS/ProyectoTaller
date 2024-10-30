# presentation/views/trabajador_view.py
from django.shortcuts import render, redirect, get_object_or_404
from AppProyecto.models import Trabajador, Genero
from django.contrib import messages
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
        genero_id = request.POST.get('genero')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')

        # Asegúrate de que el ID del género esté presente
        genero = Genero.objects.get(id_genero=genero_id) if genero_id else None

        # Verificar si el trabajador con el mismo RUT ya existe
        if Trabajador.objects.filter(rut=rut).exists():
            messages.error(request, f'El RUT {rut} ya está registrado para otro trabajador.')
            generos = Genero.objects.all()
            return render(request, 'Trabajadores/trabajador_create.html', {'generos': generos})

        # Crear el trabajador
        try:
            trabajador = Trabajador(
                nombre=nombre,
                rut=rut,
                genero=genero,
                direccion=direccion,
                telefono=telefono
            )
            trabajador.save()
            messages.success(request, 'Trabajador creado exitosamente.')
            return redirect('trabajador_list')
        except IntegrityError:
            messages.error(request, 'Error al crear el trabajador, por favor intenta de nuevo.')

    generos = Genero.objects.all()
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
