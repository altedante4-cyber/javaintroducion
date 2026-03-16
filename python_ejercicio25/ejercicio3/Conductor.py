from abc import ABC, abstractmethod
from datetime import time , date , datetime 
class Vehiculo:
    def __init__(self,matricula,antiguedad_coche):
        self.matricula = matricula
        self.antiguedad_coche  = antiguedad_coche

    @abstractmethod
    def calcular_seguro(self):

        pass

    @abstractmethod
    def seguro_terceros(self):
        pass 




class Conductor:

    def __init__(self,nombre,nif,anio_nacimiento,anio_alta_carnet,puntos_carnet):
        self.nombre = nombre
        self.nif = nif
        self.anio_nacimiento=anio_nacimiento
        self.anio_alta_carnet = anio_alta_carnet
        self.puntos_carnet = puntos_carnet

    
class Moto(Vehiculo):

    def __init__(self,matricula,antiguedad_coche , conductor ):
        super().__init__(matricula,antiguedad_coche)
        self.conductor = conductor 
    def calcular_seguro(self):
        
        pass


    def seguro_terceros(self):
        
        total = 200
        #pude acceder a sus puntos del conducto sin un geter 
        atributo_puntos_carnet= self.conductor.puntos_carnet
        anio_conducto_carnet = self.conductor.anio_nacimiento
        anio_fecha_carnet = self.conductor.anio_alta_carnet 
        if atributo_puntos_carnet <= 8 :
            total += 150
        if anio_conducto_carnet <= 24 :
            total += 25

        if anio_fecha_carnet <=2:
             total += 50


        return total 
    
        
    def __str__(self):
        return (f"VEHICULO: Moto. Matricula: {self.matricula}. "
            f"Año de compra: {self.antiguedad_coche} \n"
            f"Conductor: {self.conductor.nombre}. "
            f"Edad: {self.conductor.anio_nacimiento}. "
            f"Puntos: {self.conductor.puntos_carnet} \n"
            f"Precio del seguro a todo riesgo: {self.seguro_terceros()} \n"
            f"No se hacen seguros a todo riesgo a motos ")




class Coche(Vehiculo):
    
    def __init__(self,matricula,antiguedad_coche, conductor ):
        super().__init__(matricula,antiguedad_coche)
        self.conductor = conductor 

    def calcular_seguro(self):
        
        #realisamos el calculo del seguro  primero tenemos que recoger el anio en que se compro el coche  para ver si le incrementamos 400 o 500 o 700 el primer anio 400
        # el segundo 500 y el tercero 700
       anio = datetime.now().date().year
       diferencia = anio - self.antiguedad_coche
       total = 0 
       
       if diferencia < 0 : return 


       match(diferencia):
            case 1:
                total = 400 
    
            case 2 :
                total= 500
           
            case 3 :
                total = 700 
            case _ :
                total = 250 * diferencia 

    
       return total


    def seguro_terceros(self):
        
        total = 250
        #pude acceder a sus puntos del conducto sin un geter 
        atributo_puntos_carnet= self.conductor.puntos_carnet
        anio_conducto_carnet = self.conductor.anio_nacimiento
        anio_fecha_carnet = self.conductor.anio_alta_carnet 
        if atributo_puntos_carnet <= 8 :
            total += 100 
        if anio_conducto_carnet <= 24 :
            total += 50 

        if anio_fecha_carnet <=2:
             total += 75


        return total 

    
    def __str__(self):
        return (f"VEHICULO: coche. Matricula: {self.matricula}. "
            f"Año de compra: {self.antiguedad_coche} \n"
            f"Conductor: {self.conductor.nombre}. "
            f"Edad: {self.conductor.anio_nacimiento}. "
            f"Puntos: {self.conductor.puntos_carnet} \n"
            f"Precio del seguro a todo riesgo: {self.calcular_seguro()} \n"
            f"Precio del seguro a terceros: {self.seguro_terceros()}")

conductor1 = Conductor("miki","12345678",22,39,4)

moto = Moto(4566,2024,conductor1)
coche = Coche(1234,2022,conductor1)


print(moto)