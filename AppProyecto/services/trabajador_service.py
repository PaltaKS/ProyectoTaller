from AppProyecto.repositories.trabajador_repository import TrabajadorRepository
from AppProyecto.services.usuario_service import UsuarioService

class TrabajadorService:

    @staticmethod
    def listar_trabajadores():
        return TrabajadorRepository.obtener_todos()


    @staticmethod
    def obtener_trabajador(rut):
        return TrabajadorRepository.obtener_por_rut(rut)

    
    @staticmethod
    def crear_trabajador_usuario(data):
    # Validación de campos requeridos
        campos_requeridos = ['rut', 'nombre', 'genero_id', 'direccion', 'telefono']
        for campo in campos_requeridos:
            if not data.get(campo):
                raise ValueError(f"El campo {campo} es obligatorio.")

        # Validación específica del RUT
        trabajador_existente = TrabajadorRepository.obtener_por_rut(data['rut'])
        if trabajador_existente:
            raise ValueError(f"El RUT {data['rut']} ya está asignado a un trabajador existente.")

        # Validaciones de longitud
        if len(data['nombre']) > 100:
            raise ValueError("El nombre no puede exceder los 100 caracteres")
        if len(data['direccion']) > 200:
            raise ValueError("La dirección no puede exceder los 200 caracteres")

        # Si pasa todas las validaciones, crear el trabajador
        trabajador = TrabajadorRepository.create_trabajador(data)
        
        try:
            # Crear automáticamente el usuario
            nombre_usuario = f"{trabajador.nombre.split()[0].lower()}{trabajador.rut[:4]}"
            contraseña = f"12345"
            email = f"{nombre_usuario}@logisticaqk.cl"
            
            # En lugar de crear un diccionario, pasamos los argumentos directamente
            usuario = UsuarioService.crear_usuario(
                nombre_usuario=nombre_usuario,
                trabajador_id=trabajador.rut,  # Usando rut como ID
                rol_id=3,  # ID del rol por defecto
                contrasena=contraseña,
                email=email
            )
            
        except Exception as e:
            raise ValueError(f"Error al crear usuario automático: {str(e)}")

        return trabajador



    @staticmethod
    def actualizar_trabajador(rut, data):
        return TrabajadorRepository.actualizar_trabajador(rut, data)



    @staticmethod
    def eliminar_trabajador(rut):
        return TrabajadorRepository.eliminar_trabajador(rut)
    
    
    def listar_trabajadores_por_genero():
        """
        Procesa los datos obtenidos desde el repository si es necesario.
        """
        return TrabajadorRepository.obtener_trabajadores_por_genero()


    