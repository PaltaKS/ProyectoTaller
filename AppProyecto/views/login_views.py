from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from AppProyecto.forms.login_form import LoginForm
from AppProyecto.models import Usuario

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data['nombre_usuario']
            contrasena = form.cleaned_data['contrasena']
            
            # Obtener el usuario por nombre de usuario
            try:
                usuario = Usuario.objects.get(nombre_usuario=nombre_usuario)
            except Usuario.DoesNotExist:
                form.add_error(None, "Credenciales inválidas.")
                return render(request, 'login.html', {'form': form})

            # Verificar la contraseña
            if check_password(contrasena, usuario.contrasena):
                # Almacenar información del usuario en la sesión
                request.session['user_id'] = usuario.id_usuario
                
                # Redirigir al home después de validar el login
                return redirect('home')  # Asegúrate de que 'home' esté definido en tus URLs
            else:
                form.add_error(None, "Credenciales inválidas.")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})



