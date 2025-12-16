def mifuncion(x,y):
    return x + y 
#otra manera para saber que tipo de datos es x y tipo de dato


def mifuncion(x:int , y:int ) -> int :  #no sireve de nada es como para que el programador sepa que va a devolver 
    return x + y 

# si yo defino una viriable dentro de la funcion ya no existe fuera de esa funcion  
def mifuncion(x:int , y:int ) -> int :
    print(variable)
    variable2 = 777  # ESTO ES DE AMBITO LOCAL ES DECIR QUE SOLO SE PUEDE UTILIZAN EN ESTA FUNCION 
    return x + y 


variable = 555 # ESTO ES DE AMBIO GLOBAL 
print(mifuncion(2,3))
print(mifuncion("hoa","mundo"))

#devovel masde un valor en python

def mifuncion() :

    return "Jose Maria",57,2400.44

nombre,edad,sueldo = mifuncion()
print(nombre, " -  " , edad ,  " - " , sueldo )


