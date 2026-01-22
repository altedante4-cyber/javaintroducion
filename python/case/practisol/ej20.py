"""
Docstring for ej20
Problema de Práctica 3: Generador de Acrónimos y Longitud (Combinación de Lógica)
Este ejercicio combina el acceso a caracteres individuales y el cálculo de longitud de una manera diferente.

Descripción: Escribe un programa que tome una frase y genere un acrónimo. Luego, debe mostrar la frase original y el acrónimo junto con el promedio de longitud de las palabras de la frase.
Reglas de Salida:

El acrónimo se forma tomando la primera letra de cada palabra y debe estar en mayúsculas (LDPP).

El programa debe calcular el promedio de la longitud de todas las palabras (sin contar espacios ni el acrónimo).

Formato de Salida: [Frase Original] -> Acrónimo: [Acrónimo] - Longitud promedio de palabra: [Promedio con dos decimales]

Ejemplo de Ejecución: | Entrada | Resultado | | :--- | :--- | | frase_original = "Lenguaje de Programación en Python" | Lenguaje de Programación en Python -> Acrónimo: LDPP - Longitud promedio de palabra: 7.75 |


"""
frase_original = "Lenguaje de Programación en Python"


dividir = frase_original.split()

acronimos = ""
for i in range(len(dividir)):

    acronimos += dividir[i][0]


    
acronimos_mayuscula = acronimos.upper()

print(acronimos_mayuscula)


#sacar longitud

suma_longitudes = 0

for palabra in dividir :

    suma_longitudes += len(dividir)


numero_palabras = len(dividir)

if numero_palabras > 0 :
    promedio = suma_longitudes / numero_palabras
else:
    promedio = 0.0

resultado = (
        f"{frase_original} -> Acrónimo: {acronimos_mayuscula} - "
        f"Longitud promedio de palabra: {promedio:.2f}"
    )

print(resultado)

