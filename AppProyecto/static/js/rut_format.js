function limpiarRut(rut) {
    // Elimina puntos y guión, y convierte a mayúsculas
    return rut.replace(/\./g, '').replace(/-/g, '').toUpperCase();
}

function formatearRut(input) {
    let rut = limpiarRut(input.value);
    if (rut.length > 1) {
        let cuerpo = rut.slice(0, -1);
        let dv = rut.slice(-1);
        input.value = cuerpo.replace(/\B(?=(\d{3})+(?!\d))/g, ".") + '-' + dv;
    }
}

function calcularDigitoVerificador(rut) {
    let suma = 0;
    let multiplicador = 2;
    for (let i = rut.length - 1; i >= 0; i--) {
        suma += parseInt(rut[i]) * multiplicador;
        multiplicador = multiplicador < 7 ? multiplicador + 1 : 2;
    }
    let dv = 11 - (suma % 11);
    if (dv === 11) return '0';
    if (dv === 10) return 'K';
    return dv.toString();
}

function validarRut(input) {
    let rut = limpiarRut(input.value);
    if (rut.length < 2) {
        input.setCustomValidity("RUT demasiado corto");
        return;
    }

    let cuerpo = rut.slice(0, -1);
    let dv = rut.slice(-1).toUpperCase();
    let dvCalculado = calcularDigitoVerificador(cuerpo);

    if (dvCalculado !== dv) {
        alert("RUT inválido");
        input.setCustomValidity("RUT inválido");
    } else {
        alert("Rut Valido")
        input.setCustomValidity(""); // RUT válido
    }
}
