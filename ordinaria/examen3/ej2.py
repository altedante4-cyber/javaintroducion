def elMasInteligente(*personajes):
    dico = {}

    for i in personajes:

        dico[i[0]] = i[4]

    maximo = max(dico , key=lambda x:x[1] )
    
    for i in personajes:

        if i[0] == maximo:
            print(i)
def estaVivo(personaje):

    return  personaje[5] > 0 


def ataque(personaje1,personaje2):
    daño_inflinjido_personaje1 = personaje1[4] / 2 
    personaje2[5] = personaje2[5] - daño_inflinjido_personaje1
    
def recuperarResistencia(personaje,numerovida):
    pass 
personaje1 = ["Ines Perado", "Bardo", "Humano", 59, 41, 118]
personaje2 = ["Ricardo Borriquero", "Mago", "Elfo", 90, 10, 180]

print(personaje2)
ataque(personaje1,personaje2)
print(personaje2)
