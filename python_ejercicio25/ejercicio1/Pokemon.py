import random   
class Pokemon:
    peso_altura_definir = ["mayor","menor"]

    def __init__(self , codigo , nombre , *tipos):
        self.codigo = codigo 
        self.nombre = nombre
     
        tipos_lista = tipos[0].split(",")
        #en tipos de lista estaba obteniendo lista de lista es decir una lista dentro de otra lista por ende tengo que poner el 0 ojo con eso un ejemplo de como estaba saliendo
        #[['electrico', 'agua']]

        if  len(tipos_lista) == 2 :
            self.tipos = tipos
        else:
            self.tipos = 0 

        self.peso = random.choice(self.peso_altura_definir)
        self.altura = random.choice(self.peso_altura_definir) 



    


    #validar los tipos de pokemos solo puede ser 1 o dos no pueden haber mas  quiero saber como poner solo setter y no getter y setter con el property si se puede claro

    def __str__(self):

        return f"CODIGO | {self.codigo} NOMBRE | {self.nombre}  TIPOS | {self.tipos}  PESO | {self.peso}  ALTURA | {self.altura } "


class Entrenador:
    def __init__(self,nombre):
        self.nombre = nombre 

    
    def __str__(self):
        return f"El nombre del entrenador es  {self.nombre}"


    

class Equipo :

    def __init__(self,poke1,poke2,poke3,entrenador ):

            self.poke1 = poke1
            self.poke2 = poke2
            self.poke3 = poke3
            self.entrenador = entrenador 

    


    def __str__(self):

        return f"entrenador {self.entrenador} \n  {self.poke1} \n {self.poke2} \n {self.poke3}"         




poke1 = Pokemon(12345,"miki","electrico,agua")
poke2 = Pokemon(23443,"axel","perico,cafre")
poke3 = Pokemon(59696,"peredo","leche,agua")
entrenador = Entrenador("benito malvini")

equipo1 = Equipo(poke1,poke2,poke3,entrenador)

print(equipo1)

