class Socio:
    def __init__(self,nombre,apellido , edad , fecha_alta , Gimnasio,Clase ):
         self.__nombre = nombre
         self.__apellido = apellido
         self.__edad = edad
         self.__fecha_alta = fecha_alta
         self.__Gimnasio = Gimnasio
         self.__Clase = Clase 

    
    def __str__(self):
        return f"{self.__nombre}  {self.__apellido} {self.__edad}  {self.__fecha_alta}"


class Instructor:
    def __init__(self,nombre,apellido , especialidad , Clase ):
        self.__nombre = nombre
        self.__apellido = apellido
        if especialidad in ["Musculacion", "Spinnin" ,"Yoga"]:
            self.__especialidad = especialidad
        else:
            print("error")
    @property
    def nombre(self):
        return self.__nombre        
    
class Clase:

    def __init__(self,nombre_clase , Instructor , duracion_minutos , hora_inicio ):
        self.__nombre_clase = nombre_clase
        self.__Instructor = Instructor
        self.__duracion_minutos = duracion_minutos
        self.__hora_inicio = hora_inicio 
        self.__lista_socios = []
    def agregar_socio_clase(self,Socio):
        self.__lista_socios.append(Socio)

    def cancelar_inscripcion_socio(self,Socio):
        if Socio  in self.__lista_socios:
            self.__lista_socios.remove(Socio)
        else:
            self.__lista_socios=None 

    def mostrar_informacion_clase(self):
        print(f" Nombre clase {self.__nombre_clase} Instructor {self.__Instructor.nombre} Duracion_Minutos {self.__duracion_minutos} hora_inicio {self.__hora_inicio}")
        print("==LISTA SOCIOS==")
        for i in self.__lista_socios:
            print(f"{i.__str__()}")

    def __str__(self):
        return f"Nombre {self.__nombre_clase} Instructor {self.__Instructor.nombre} duracion_minutos {self.__duracion_minutos} hora_inicio {self.__hora_inicio}"


class Gimnasio :
    def __init__(self,nombre):
        self.__nombre = nombre
        self.__lista_clases=[]
    
    def agregar_clase(self,clase):
        self.__lista_clases.append(clase)


    def listar_clases_gimnasio(self):
        for i in self.__lista_clases:
            print(i.__str__())

gimnasio1 = Gimnasio("FitLife")
# Crear instructores
instructor1 = Instructor("Carlos", "García", "Musculacion",None )
instructor2 = Instructor("Ana", "Martínez", "Spinning",None)
instructor3 = Instructor("Luis", "Pérez", "Yoga",None )
# Crear clases
clase1 = Clase("Spinning 9h", instructor2, 60, "09:00")
clase2 = Clase("Musculacion 10h", instructor1, 90, "10:00")
clase3 = Clase("Yoga 11h", instructor3, 60, "11:00")
# Agregar clases al gimnasio (método de instancia)
gimnasio1.agregar_clase(clase1)
gimnasio1.agregar_clase(clase2)
gimnasio1.agregar_clase(clase3)
# Crear socios
socio1 = Socio("Juan", "López", 25, "2026-01-15", None, None)
socio2 = Socio("María", "Sánchez", 30, "2026-02-01", None, None)
socio3 = Socio("Pedro", "Gómez", 22, "2026-02-10", None, None)
# Inscribir socios en clases
clase1.agregar_socio_clase(socio1)
clase1.agregar_socio_clase(socio2)
clase2.agregar_socio_clase(socio3)
# Mostrar información de una clase
print("=== INFORMACIÓN CLASE SPINNING ===")
clase1.mostrar_informacion_clase()

# Cancelar inscripción
print("\n=== CANCELAR INSCRIPCIÓN DE MARÍA ===")
clase1.cancelar_inscripcion_socio(socio2)
clase1.mostrar_informacion_clase()

# Listar todas las clases del gimnasio
print("\n=== LISTA DE CLASES DEL GIMNASIO ===")
gimnasio1.listar_clases_gimnasio()y

clase1.mostrar_informacion_clase()
