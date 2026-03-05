import random 

def mostrar_preguntas():
    # el shufle se utiliza para mesclar los elementos de una lista basicamente
    random.shuffle(preguntas)

    elegir_pregunta = random.choice(preguntas) #esto nos devuelve un diccionario
    
    listar_opciones = ""


    for i in elegir_pregunta['opciones']:
         listar_opciones += i  + '  '

    #para hacerlo bueno que directamente vaya en el print bien sacamos las opciones
    #ahora ese diccionario hay que mostrarlo con su pregunta
    for  i in preguntas:
         if i['preguntas'] == elegir_pregunta['preguntas']:
              print(f"PREGUNTA {i['preguntas']:>20}  | OPCIONES {listar_opciones} ")

    return elegir_pregunta['correcta']

def Aprobado_Suspendido(numero:int):

    return numero >= 5

    
preguntas = [
    {'preguntas':'dime el verbo tobe ','opciones':['a.do while','b.segundo','c.tercero','d.cuarto'] , 'correcta':2},
    {'preguntas':'dime el la forma pythonic ','opciones':['a.do while','b.segundo','c.tercero','d.cuarto'] , 'correcta':1},
    {'preguntas':'dime objeto java  ','opciones':['a.do while','b.segundo','c.tercero','d.cuarto'] , 'correcta':3},
    {'preguntas':'dime objeto en python ','opciones':['a.do while','b.segundo','c.tercero','d.cuarto'] , 'correcta':0},
    {'preguntas':'dime el sistemas  ','opciones':['a.do while','b.segundo','c.tercero','d.cuarto'] , 'correcta':1},
    {'preguntas':'dime lenguaje de marcas ','opciones':['a.do while','b.segundo','c.tercero','d.cuarto'] , 'correcta':2},
    {'preguntas':'dime desarrollo aplicacion','opciones':['a.do while','b.segundo','c.tercero','d.cuarto'] , 'correcta':1},
    {'preguntas':'dime bitcoin ','opciones':['a.do while','b.segundo','c.tercero','d.cuarto'] , 'correcta':3},
]


contador = 0

contador_aciertos = 0 
contador_fallos = 0 
while contador != 8:
     
    #validacion que el usuario introdusca valores entre 1 y 4 sobre la resupues
    acertador = False
    solucion = mostrar_preguntas()    # la solucion hay que convertirla por que va del 1 al 4 no del 0 al 3 0 1 2 3 
    solucion_correcta = solucion
    match (solucion):
        case 0 :
            solucion_correcta = 1
        case 1 :
            solucion_correcta = 2 
        case 2 :
            solucion_correcta = 3 
        case 3 :
            solucion_correcta = 4 
    
             
    while not acertador:       

        usuario = int(input("Introdusca la respuesta del 1-4 "))

        if  usuario >= 1 and usuario <=4 :
            acertador = True

        if not acertador:
            print("Vuelva a intentarlo")
        
    if acertador and usuario == solucion_correcta :
        contador_aciertos += 1
        print("has acertado")
    else:
        contador_fallos += 1
        print("no has acertado")
    
    contador += 1 
cadena = ""
a = Aprobado_Suspendido(contador_aciertos)
if a :
    cadena += "APROBADO"
else:
    cadena += "SUSPENDIDO"
print("*"*40)
print(f"{'ESTADISTICAS':^30}")
print(f"ACIERTOS QUE TUBISTE ES DE {contador_aciertos}")
print(f"FALLOS QUE TUBISTE ES DE {contador_fallos}")
print(f"USTED HA {cadena}")