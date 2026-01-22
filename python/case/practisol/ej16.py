"""
3. Queremos hacer un programa en Python que construya una cadena de texto a partir de otras dos
ya existentes (y que no se meten por teclado, sino que tienen que estar definidas como variables en
tu código). Las cadenas cuentan con la siguiente estructura:
 La primera de ellas tiene dos palabras separadas por un espacio en blanco
 La segunda tiene dos palabras separadas por un guión
Tu cadena resultante debería de hacer una composición con esos dos textos y mostrar, al final, la
longitud total de ambas cadenas entre paréntesis como se verá en el ejemplo que sigue.
Suponiendo que las dos cadenas de las que se parte son las siguientes:

La ejecución de tu programa debería de mostrar esto:

Como ves, aparecen primero las palabras que van en segundo lugar de ambas separadas por un
guión y luego las palabras que van en primer lugar separadas por un espacio. Finalmente, un
paréntesis con la longitud total que suman ambas.
NOTAS IMPORTANTES:
 Ambas cadenas cumplen con el formato que se pide, es decir, son dos palabras separadas
por un espacio y un guión respectivamente.
 Tu programa no solo debe de producir la salida que se pide por consola, sino que tiene que
producir y almacenar una tercera variable de tipo String con el contenido que luego se
muestra en consola.

"""
texto1 = "Examen 1T01"
texto2 = "Octubre-2025"
# tercera variable resultado =>Resultado: 1T01-2025 Examen Octubre (23)

#1.dESCOMPONER TEXTO1 (separado por espacio)

#Examen 1T01 => [Examen , 1t01]

partes_t1 = texto1.split(' ')

palabra1_t1 = partes_t1[0] #Examen
palabra2_t1 = partes_t1[1] #1T01

#Descomponer texto 2 separado por guion
#octubre-2025 

partes_t2 = texto2.split('-')

palabra1_t2 = partes_t2[0] 
palabra2_t2 = partes_t2[1]

#calcular la longitud total

longitud_total = len(texto1) + len(texto2)

#4contruir la cadena de resultado final(recordenada)

resultado_compuesto = (
    f"{palabra2_t1} - {palabra2_t2}"
    f"{palabra1_t1} "
    f"{palabra1_t2} "
    f"({longitud_total})"
)


#almacenar el resultado en la variable final

resultado = f"resultado {resultado_compuesto}"

#mostra la salida final

print(resultado)
