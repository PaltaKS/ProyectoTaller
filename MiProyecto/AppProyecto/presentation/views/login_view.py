from django.shortcuts import render, redirect
from AppProyecto.data.repositories.user_repository import UserRepository
from django.contrib.auth.hashers import check_password


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('nombre_usuario')
        password = request.POST.get('contrasena')

        print(f"Intento de login con usuario: {username}")  # Mensaje de depuración

        user_repo = UserRepository()
        user = user_repo.get_user_by_username(username)

        if user:
            print(f"Usuario encontrado: {user['nombre_usuario']}")  # Mensaje de depuración
            if check_password(password, user['contrasena']):
                print(f"Login exitoso para el usuario: {username}")  # Mensaje de depuración

                # Redirigir según el rol
                print(f"Rol del usuario: {user['rol_id']}")  # Supongamos que almacenas el rol como ID por ahora

                # Aquí, debes implementar la lógica para obtener el rol basado en `rol_id`
                # Esto podría ser una consulta adicional a la base de datos
                if user['rol_id'] == 1:  # ADMIN
                    print("Redirigiendo a ADMIN")
                    return redirect('admin_dashboard')  # URL a la vista de ADMIN
                elif user['rol_id'] == 2:  # RRHH
                    return redirect('rrhh_home')  # URL a la vista de RRHH
                elif user['rol_id'] == 3:  # EMPLEADO
                    return redirect('empleado_home')  # URL a la vista de EMPLEADO
                else:
                    print("Rol no reconocido.")  # Mensaje de depuración
                    return render(request, 'Login/login.html', {'error': 'Rol no reconocido.'})
            else:
                print(f"Contraseña incorrecta para el usuario: {username}")  # Mensaje de depuración
        else:
            print(f"Usuario no encontrado: {username}")  # Mensaje de depuración

        print(f"Contraseña ingresada: {password}")  # Mensaje de depuración
        print(f"Contraseña almacenada (hash): {user['contrasena'] if user else 'N/A'}")
        return render(request, 'Login/login.html', {'error': 'Nombre de usuario o contraseña incorrectos.'})

    return render(request, 'Login/login.html')
  # Renderiza en la plantilla de login
