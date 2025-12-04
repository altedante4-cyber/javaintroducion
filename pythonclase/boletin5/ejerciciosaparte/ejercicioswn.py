
"""
Escribe un programa que valide un DNI español.
Debe tener 8 dígitos + 1 letra. La letra se calcula con el módulo 23.
Tabla letras: TRWAGMYFPDXBNJZSQVHLCKE
Ejemplo:
Introduce DNI: 12345678Z → DNI válido
Introduce DNI: 12345678A → DNI inválido
"""
dni = input("Introduce DNI: ")


letra = dni[-1:].upper
letra_validas = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
numeros = dni[:-1]

    












