import random
def damefuerza():
       return random.randint(50,101)
        


def dameinteligencia(fuerza):
        return 100 - fuerza 

def dameresistencia(fuerza):
        return fuerza * 2 



def construyePersonaje(nombre,adjetivos,clases,razas):


    
    elegirnombre = random.choice(nombre)
    elegir_adjetivos = random.choice(adjetivos)
    elegir_clase = random.choice(clases)
    elegir_raza = random.choice(razas)

    a = [elegirnombre , elegir_adjetivos]
    fuerza = damefuerza()
    inteligencia = dameinteligencia(fuerza)
    resistencia = dameresistencia(fuerza)
    return [ " ".join(a), elegir_clase , elegir_raza ,  fuerza,inteligencia, resistencia ]


nombres=["Gimli", "Legolás", "Frodo", "Gandalf"]
adjetivos=["Barbarroja", "Pies Grandes", "el Gris", "Piedradura", "el Deslumbrante"]
clases=["Mago", "Guerrero", "Ladrón", "Bardo"]
razas=["Elfo", "Humano", "Enano"]

personaje = construyePersonaje(nombres,adjetivos,clases,razas)
print(personaje)