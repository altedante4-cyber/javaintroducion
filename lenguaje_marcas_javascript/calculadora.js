const num1 = document.getElementById('num1');
const num2 = document.getElementById('num2');
const resultado = document.getElementById('resultado');
const buttons = document.querySelectorAll('button');

for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function() {
        const n1 = parseFloat(num1.value);
        const n2 = parseFloat(num2.value);

        if (isNaN(n1) || isNaN(n2)) {
            resultado.textContent = "Resultado: Ingresa ambos números";
            return;
        }

        let res;

        switch (buttons[i].id) {
            case 'btnSumar':
                res = n1 + n2;
                break;
            case 'btnRestar':
                res = n1 - n2;
                break;
            case 'btnMultiplicar':
                res = n1 * n2;
                break;
            case 'btnDividir':
                if (n2 === 0) {
                    resultado.textContent = "Resultado: No se puede dividir por 0";
                    return;
                }
                res = n1 / n2;
                break;
        }

        resultado.textContent = "Resultado: " + res;
    });
}
