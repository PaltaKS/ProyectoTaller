from django.urls import path
from AppProyecto.views.trabajador_views import listar_trabajadores, crear_trabajador,actualizar_trabajador, eliminar_trabajador  # Trabajador
from AppProyecto.views.genero_views import listar_generos, crear_genero, actualizar_genero, eliminar_genero # Genero
from AppProyecto.views.usuario_view import listar_usuarios, crear_usuario, actualizar_usuario, eliminar_usuario  # Usuarios
from AppProyecto.views.contacto_emergencia_views import listar_contactos, crear_contacto, editar_contacto, eliminar_contacto  #Contactos de Emergencia
from AppProyecto.views.carga_familiar_views import listar_cargas_familiares, crear_carga_familiar, editar_carga_familiar, eliminar_carga_familiar # Carga Familiar
from AppProyecto.views.datos_laborales_view import lista_datos_laborales, crear_datos_laborales, editar_datos_laborales, eliminar_datos_laborales # Datos Laborales
from AppProyecto.views.resetear_contrasena_views import recuperar_contrasena, restablecer_contrasena # Resetear Contrasena
from AppProyecto.views.home_views import home_view
from AppProyecto.views.login_views import login_view
from AppProyecto.views.logout_view import logout_view


urlpatterns = [
    path('', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),  # La página de inicio después del login
    path('logout/', logout_view, name='logout'),  # URL para cerrar sesión

    path('trabajadores/', listar_trabajadores, name='listar_trabajadores'),
    path('trabajadores/crear/', crear_trabajador, name='crear_trabajador'),
    path('trabajadores/actualizar/<str:rut>/', actualizar_trabajador, name='actualizar_trabajador'),
    path('trabajadores/eliminar/<str:rut>/', eliminar_trabajador, name='eliminar_trabajador'),

    path('generos/', listar_generos, name='lista_generos'),
    path('generos/crear/', crear_genero, name='crear_genero'),
    path('generos/actualizar/<int:id_genero>/', actualizar_genero, name='actualizar_genero'),
    path('generos/eliminar/<int:id_genero>/', eliminar_genero, name='eliminar_genero'),

    path('usuarios/', listar_usuarios, name='lista_usuarios'),
    path('usuarios/crear/', crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:id_usuario>/', actualizar_usuario, name='actualizar_usuario'),
    path('usuarios/eliminar/<int:id_usuario>/', eliminar_usuario, name='eliminar_usuario'),

    path('contactos/nuevo/', crear_contacto, name='crear_contacto'),
    path('contactos/', listar_contactos, name='listar_contactos'),
    path('contactos/editar/<int:id_contacto>/', editar_contacto, name='editar_contacto'),
    path('contactos/eliminar/<int:id_contacto>/', eliminar_contacto, name='eliminar_contacto'),

    path('cargas_familiares/', listar_cargas_familiares, name='listar_cargas_familiares'),
    path('cargas_familiares/nuevo/', crear_carga_familiar, name='crear_carga_familiar'),
    path('cargas_familiares/editar/<int:carga_id>/', editar_carga_familiar, name='editar_carga_familiar'),
    path('cargas_familiares/eliminar/<int:carga_id>/', eliminar_carga_familiar, name='eliminar_carga_familiar'),

    path('datos_laborales/', lista_datos_laborales, name='lista_datos_laborales'),
    path('datos_laborales/crear/', crear_datos_laborales, name='crear_datos_laborales'),
    path('datos_laborales/editar/<int:id_datos_laborales>/', editar_datos_laborales, name='editar_datos_laborales'),
    path('datos_laborales/eliminar/<int:id_datos_laborales>/', eliminar_datos_laborales, name='eliminar_datos_laborales'),

    path('recuperar-contrasena/', recuperar_contrasena, name='recuperar_contrasena'),
    path('restablecer-contrasena/<str:token>/', restablecer_contrasena, name='restablecer_contrasena'),

]