class pokemon:
    numpokemon = 0 

    @classmethod
    def coleccion(cls):
        print("Tienes",cls.numpokemon , " en tu coleccion ")

    def __init__(self,numero, nombre, *tipos):
        self.__numero = numero 
        self.__nombre = nombre
        self.__tipos = tipos 
        pokemon.numpokemon += 1 
    #*tipo = lo guarda como un numero variable de tipo 


    @property
    def nombre(self):

        return self.__nombre
    

    def verPokemon(self):
        print("#",self.__numero , "-" , self.__nombre)

        print(f"Tipo(s) {self.__tipos}")

