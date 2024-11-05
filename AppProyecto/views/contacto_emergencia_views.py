from django.shortcuts import render, redirect, get_object_or_404
from AppProyecto.models import ContactoEmergencia, Trabajador

def crear_contacto(request):
    trabajadores = Trabajador.objects.all()  # Obtener todos los trabajadores

    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.POST.get('nombre')
        relacion = request.POST.get('relacion')
        telefono = request.POST.get('telefono')
        trabajador_rut = request.POST.get('trabajador')  # Suponiendo que estás usando rut

        # Comprobar si el trabajador existe
        trabajador = Trabajador.objects.filter(rut=trabajador_rut).first()  # Buscar el trabajador por rut

        if trabajador:  # Si el trabajador existe
            # Crear y guardar el contacto de emergencia
            nuevo_contacto = ContactoEmergencia(
                nombre=nombre,
                relacion=relacion,
                telefono=telefono,
                trabajador=trabajador  # Asignar el trabajador encontrado
            )
            nuevo_contacto.save()  # Guardar el contacto
            return redirect('listar_contactos')  # Redirigir a la lista de contactos
        else:
            # Manejar el caso donde el trabajador no existe
            return render(request, 'contactos_emergencia/formulario.html', {
                'trabajadores': trabajadores,
                'error': "El trabajador seleccionado no existe."  # Mensaje de error
            }) 

    return render(request, 'ContactoEmergencia/formulario.html', {'trabajadores': trabajadores})  # Renderizar el formulario



# Listar Contactos de Emergencia
def listar_contactos(request):
    contactos = ContactoEmergencia.objects.all()
    return render(request, 'ContactoEmergencia/lista.html', {'contactos': contactos})

# Editar Contacto de Emergencia
def editar_contacto(request, id_contacto):
    contacto = get_object_or_404(ContactoEmergencia, id_contacto=id_contacto)

    if request.method == 'POST':
        contacto.nombre = request.POST.get('nombre')
        contacto.relacion = request.POST.get('relacion')
        contacto.telefono = request.POST.get('telefono')
        contacto.trabajador_id = request.POST.get('trabajador')

        contacto.save()
        return redirect('listar_contactos')

    else:
        trabajadores = Trabajador.objects.all()
        return render(request, 'ContactoEmergencia/formulario.html', {'contacto': contacto, 'trabajadores': trabajadores})

# Eliminar Contacto de Emergencia
def eliminar_contacto(request, id_contacto):
    contacto = get_object_or_404(ContactoEmergencia, id_contacto=id_contacto)

    if request.method == 'POST':
        contacto.delete()
        return redirect('listar_contactos')

    return render(request, 'ContactoEmergencia/eliminar.html', {'contacto': contacto})
