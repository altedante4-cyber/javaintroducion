texto = "el gato y el perro y el gato y el raton y el gato"
palabras = texto.split()

frecuencia = {}
for p in palabras:
    frecuencia[p] = frecuencia.get(p, 0) + 1

mas_comun = max(frecuencia, key=frecuencia.get)
frec_ordenada = dict(sorted(frecuencia.items(), key=lambda x: x[1], reverse=True))

numeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
conteo_nums = {}
for n in numeros:
    conteo_nums[n] = conteo_nums.get(n, 0) + 1

char_frec = {}
for c in "programacion":
    char_frec[c] = char_frec.get(c, 0) + 1

repetidos = {k: v for k, v in conteo_nums.items() if v > 1}

print("Frecuencia palabras:", frecuencia)
print("Mas comun:", mas_comun)
print("Ordenada:", frec_ordenada)
print("Conteo numeros:", conteo_nums)
print("Frecuencia caracteres:", char_frec)
print("Repetidos (>1):", repetidos)
