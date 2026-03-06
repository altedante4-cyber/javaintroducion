import re
#entrad de usuario 

texto = input("Introduce texto ")
#contar caracteres

total_caracteres = len(texto)
total_caracteres_sin_espacios = len(texto.replace(" " ,""))
#separa oraciones

oraciones = [oracion.strip() for oracion in  re.split(r'[.!?]',texto ) if oracion.strip()]
total_oraciones = len(oraciones)

#separar palabras 
palabras= []

for oracion in oraciones:
    palabras_oracion = [ p for p in oracion.split() if  p ] #quitar vacios
    palabras.extend(palabras_oracion)

#diferencia entre el extend y el append
# append([4,5]) agrega la lista completa como un solo elemento
# extend([4,5]) agrega cada elemento de la lista individualmente
#uso tipco oraciones = [ ["hola" , "mundo"]]  palabras = [] for oracion in oraciones palabras.extend(oracion)
total_palabras =len(palabras)

#longitud media de palabras y oraciones 
longitud_media_palabras = sum(len(p) for p in palabras ) / total_palabras if total_palabras else 0  
longitud_media_oraciones  = total_palabras / total_oraciones if total_oraciones else 0

#palabras unicas y riqueza lexica
palabras_unicas = set(palabras)
riqueza_lexica = len(palabras_unicas) / total_palabras if total_palabras else 0

#porcentaje de palabras largas (6> letras)
palabras_largas = [p for p in palabras if len(p) > 6]
porcentaje_largas = len(palabras_largas) / total_palabras * 100 if total_palabras else 0

# tres palabras mas largas sin repetir
palabras_sin_repetir = list(dict.fromkeys(palabras)) #elimina duplicados manteniendo el orden
""" list(dict.fromkeys ) list(dict.fromkeys) elimina duplicados manteniendo el orden"""
palabras_ordenadas = sorted(palabras_sin_repetir , key=len , reverse=True)
""" sorted(palabras_sin_repetid , key=len , reverse=True )"""
tres_mas_largas = palabras_ordenadas[:3]

#infrome final 
print("\n--- Informe del Texto ---")
print(f"Total de caracteres: {total_caracteres}")
print(f"Total de caracteres sin espacios: {total_caracteres_sin_espacios}")
print(f"Total de palabras: {total_palabras}")
print(f"Total de oraciones: {total_oraciones}")
print(f"Longitud media de palabras: {longitud_media_palabras:.2f} letras")
print(f"Longitud media de oraciones: {longitud_media_oraciones:.2f} palabras")
print(f"Riqueza léxica: {len(palabras_unicas)} palabras únicas ({riqueza_lexica:.2%})")
print(f"Porcentaje de palabras largas (>6 letras): {porcentaje_largas:.2f}%")
print(f"Tres palabras más largas: {', '.join(tres_mas_largas)}")