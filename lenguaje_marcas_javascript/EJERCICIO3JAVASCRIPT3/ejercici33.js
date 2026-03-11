document.getElementById('enviar').addEventListener('click', function() {
    const campos = document.querySelectorAll('input');
    let valoresDevolver = "";
    let encontradoVacio = false;

    for (let i = 0; i < campos.length; i++) {
        if (campos[i].value === "") {
            encontradoVacio = true;
            break;
        }
        
        valoresDevolver += campos[i].id + ': ' + campos[i].value + '<br>';
    }

    if (encontradoVacio) {
        alert("Debes tener todos los campos llenos");
    } else {
        alert(valoresDevolver);
        document.querySelectorAll('input').forEach(input => input.value = "");
        
    }
});
