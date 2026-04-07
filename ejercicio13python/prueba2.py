from abc import ABC,abstractmethod

class Material(ABC):
    def __init__(self,titulo,artista,genero,anio_lanzamiento):
        self.__titulo = titulo
        self.__artista= artista
        self.__genero = genero
        self.__anio_lanzamiento = anio_lanzamiento

    @abstractmethod
    def get_duracion(self):
        pass
    @abstractmethod
    def get_tipo_material(self):
        pass

    def __str__(self):
        return f"Titulo {self.__titulo} Artista {self.__artista} Genero {self.__genero} anio_lanzamienot {self.__anio_lanzamiento}"
    

    def __eq__(self,other):

        return self.__titulo== other.titulo  and self.__artista == other.artista 

    def __len__(self):
        return int(self.get_duracion())

class Cancion(Material):

    def __init__(self,titulo,artista,genero,anio_lanzamiento,albun,duracion_segundos,es_explicito):
         super().__init__(titulo,artista,genero,anio_lanzamiento)
         self.__albun = albun
         self.__duracion_segundos = duracion_segundos
         self.__es_explicito = es_explicito
        
    def get_duracion(self):
        return self.__duracion_segundos / 60 
    
    def get_tipo_material(self):
        return "DIGITAL"
    
    @classmethod
    def crear_desde_diccionario(cls,datos):
        return cls (
             datos["titulo"],
             datos["artista"],
             datos["genero"],
             datos["anio_lanzamiento"],
             datos["albun"],
             datos["duracion_segundos"],
             datos["es_explicito"]
        )


class Album(Material):
    def __init__(self,titulo,artista,genero,anio_lanzamiento , sello_discografico ):
        super().__init__(titulo,artista,genero,anio_lanzamiento)
        self.__canciones = []
        self.__sello_discografico = sello_discografico
    
    def agregar_cancion(self,cancion):
        self.__canciones.append(cancion)

    def eliminar_cancion(self,cancion):
        if cancion not in self.__canciones:
             raise ValueError("Error no se encontro la cancion")

        self.__canciones.remove(cancion)

    def get_duracion(self):
        contador = 0 
        for i in self.__canciones:
            contador += i.get_duracion()

        return contador

    def get_tipo_material(self):
        return list(set(i.get_tipo_material() for i in self.__canciones))


        
        
c1 = Cancion("Imagine", "John Lennon", "Rock", 1971, "Imagine", 183, False)
print(c1.get_duracion())  # 3.05
datos = {"titulo": "Bohemian Rhapsody", "artista": "Queen", "genero": "Rock", 
         "anio_lanzamiento": 1975, "albun": "A Night at the Opera", 
         "duracion_segundos": 354, "es_explicito": False}
c2 = Cancion.crear_desde_diccionario(datos)
album = Album("Greatest Hits", "Queen", "Rock", 1981, "EMI")
album.agregar_cancion(c2)
album.eliminar_cancion(c2)