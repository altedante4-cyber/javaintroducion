cl = {'Carmelo Coton ': '5,2.5,3,3,6.2'}

lista_enteros = []

for clave, valor in cl.items():
    # 1. 'valor.split(",")' crea la lista ['5', '2.5', '3', '3', '6.2']
    numeros_en_texto = valor.split(",")
    
    # 2. Ahora debes iterar sobre esa nueva lista de textos
    for n in numeros_en_texto:
        # Convertimos cada texto a float y luego a int
        numero_entero = float(n)
        lista_enteros.append(numero_entero)

print(lista_enteros)
# Resultado: