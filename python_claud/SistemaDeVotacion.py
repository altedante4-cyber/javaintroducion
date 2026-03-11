import random 
def contar_votos():
    votos_contados = {'miki': 0, 'perci': 0, 'evo': 0, 'lara': 0}
    for i in votantes:
        if i in votos_contados:
            votos_contados[i] += 1


    return votos_contados

def calcular_porcentaje():
    votos_cont = contar_votos()

    porcentaje = {candidato:f"{(votos / 100 ) * 100:.2f}%" for candidato , votos in votos_cont.items() }


    return porcentaje



    

candidatos = ["miki","perci","evo","lara"]
votantes = [random.choice(candidatos) for _ in range(100)]



calculo_porcentaje = calcular_porcentaje()
superan_el_50porciento = any(float(valor.replace('%','')) > 50 for valor in calculo_porcentaje.values())


if not superan_el_50porciento:
    
    #porcentajes_ordenador = sorted([float(valor.replace('%','')) for valor in calculo_porcentaje.values()], reverse=True)

    #sacar_el_mas_botado = porcentajes_ordenador[0]
    #ssegundo_mas_botado = porcentajes_ordenador[1]
    # esta bien pero no es lo que buscamo por que esto solo te saca los valores no la clave necesitamos la clave y el valo

    votos_cont = contar_votos()
    ordenador = sorted(votos_cont.items() , key=lambda x:x[1] , reverse=True )
    mas_votado = ordenador[0][0]
    segundo_mas_votado = ordenador[1][0]
    mas_votado = ordenador[0]
    segundo_mas_votado= ordenador[1]

    finalistas = [ordenador[0][0] , ordenador[1][0]]
    print(f"finalistas son {finalistas} ")


    #2NUEVA VOTACION SIMULADA 
    #SOLO DAMOS A ELEGIR ENTRE LOS DOS FINALISTAS

    nuevos_votantes = [random.choice(finalistas) for _ in range(100)]

    #3contar votos de la segunda vuelta

    #usamos un diccionario por compresino para inciialisar solo a los finaliestas

    votas_segunda_vuelta = {candidato: 0 for candidato in finalistas }
    for voto in nuevos_votantes:
        votas_segunda_vuelta[voto]+= 1 

    print("Resultado segunda vuelta " , votas_segunda_vuelta)
    