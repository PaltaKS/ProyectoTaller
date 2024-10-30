from django.shortcuts import render

# Aqui se renderizan todos los HTML

# Vista para ADMIN
def admin_home_view(request):
    return render(request, 'RolesLogin/admin_home.html')

# Vista para RRHH
def rrhh_home_view(request):
    return render(request, 'roles/rrhh_home.html')

# Vista para EMPLEADO
def empleado_home_view(request):
    return render(request, 'roles/empleado_home.html')