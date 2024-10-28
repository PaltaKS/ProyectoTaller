from django.shortcuts import render
from django.shortcuts import redirect  # Importa el modelo si es necesario

def pagina_principal_view(request):
    # Puedes agregar lógica aquí para obtener datos si es necesario
    return render(request, 'Login/home.html') 

def custom_logout_view(request):
    # Lógica para cerrar sesión
    if 'id_usuario' in request.session:
        del request.session['id_usuario']
        del request.session['nombre_usuario']
    request.session.flush()
    return redirect('login')  # Ajusta 'login' según tu URL de inicio de sesión