import random 
def contar_votos( votos):

    contador_c1 = 0 
    contador_c2 =  0 
    contador_c3 = 0 
    contador_c4 = 0 

    if votos == "miki" :
        contador_c1 += 1 
    

    return contador_c1



candidatos = ["miki","perci","evo","lara"]
votantes = [random.randint(50,100) for _ in range(100)]

for i in votantes:

    simular = random.choices(candidatos)
    a = contar_votos(simular)
    print(f"votante{i} voto por  | {simular}")
print(a)

