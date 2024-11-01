from django.shortcuts import redirect

def logout_view(request):
    request.session.flush()  # Elimina todos los datos de la sesión
    return redirect('login')  # Redirigir al login

