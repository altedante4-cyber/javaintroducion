
from abc import ABCMeta, abstractmethod

class Persona(metaclass=ABCMeta):
    def __init__(self,nombre , apellidos , tlf ):
        self.nombre = nombre 
        self.apellidos = apellidos
        self.tlf = tlf 
    @abstractmethod
    def verDatos(self):
        pass 


class Profesor(Persona):
    def __init__(self,nombre , apellidos , tlf ):
        super().__init__(nombre ,apellidos , tlf  )
    
    def verDatos(self):
        print(f"nombre es {self.nombre} el apellido {self.apellidos } el telefono es {self.tlf } ")

class Alumno(Persona):

    def __init__(self,nombre,apellidos,tlf):
        super().__init__(nombre,apellidos,tlf)
    def verDatos(self):
        print(f"nombre es {self.nombre} el apellido {self.apellidos } el telefono es {self.tlf } ")



profesor=Profesor("pepe","potano",2993494)
profesor.verDatos()
alumno=Alumno("antonio","cortes",2394949)
alumno.verDatos()
