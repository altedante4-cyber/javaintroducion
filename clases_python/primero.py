class Alumno:
    def __init__(self,nom,ed,nif):
        self.__edad =  ed 
        self.nombre = nom
        self.nif = nif 


    def verDatos(self):

        print("nombre",self.nombre , "Edad" , self.__edad )
        print("NIF:  " , self.nif )

    def setEdad(self,ed):
        self.__edad = ed

    def getEdad(self):
        return self.__edad 
        
    @property # lo que indica es que vamos a definir un get 
    def edad(self):
         return self.__edad

# utilizando el doble subrallado  es para proteger 

trista = Alumno("Leadron",33,"13442")
galdeano = Alumno("Tomas Baldeano",20,"10304")
nicolle = Alumno("NIcolle",26,"232332")


#el metod geter y seter de  python es un decorador

    

trsta__edad = 55  # no nos dejaria por que  esta protegido

trista.setEdad(55)
trista.verDatos()
print(trista.getEdad())
#utilizando el decorador

print(trista.edad)

