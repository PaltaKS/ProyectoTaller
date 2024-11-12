// Función para formatear el RUT en tiempo real
function formatearRut(rutInput) {
    let rut = rutInput.value.replace(/\./g, '').replace('-', ''); // Eliminar puntos y guion

    // Permitir que el último carácter sea "K" o un número
    if (rut.length > 0) {
        let dv = rut.slice(-1).toUpperCase(); // Obtener el dígito verificador en mayúscula
        let cuerpo = rut.slice(0, -1);

        // Asegurarse de que el cuerpo solo contenga números
        if (!/^\d+$/.test(cuerpo) && cuerpo.length > 0) {
            rutInput.value = ''; // Limpiar el campo si el formato es incorrecto
            return;
        }

        // Formatear el RUT con puntos y guion
        if (cuerpo.length <= 7) {
            rutInput.value = cuerpo.replace(/^(\d{1,2})(\d{3})(\d{3})$/, '$1.$2.$3') + '-' + dv;
        } else {
            rutInput.value = cuerpo.replace(/^(\d{1,2})(\d{3})(\d{3})$/, '$1.$2.$3') + '-' + dv;
        }
    }
}
