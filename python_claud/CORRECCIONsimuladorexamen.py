import random

def mostrar_pregunta(datos_pregunta, numero_actual ):

    """Imprirme la pregunnta y devuelve la respuesta correcta ajustada (1-4)"""
    print(f"\n Pregunta{numero_actual}: {datos_pregunta{'preguntas'}}")

    #mostramos las opciones enumeradas del 1 al 4

    for i , opcion in enumerate(datos_pregunta['opciones'], 1):
        print(f" {i} . {opcion}")

    #retornamos el indice correcto +1 para que coincida con el input(1-4)

    return datos_pregunta['correcta'] + 1 

def Aprobado_Suspendido(aciertos):
    return aciertos >=  5

#-- DATOS--

preguntas = [
    {'preguntas':'¿Cuál es el verbo "to be"?','opciones':['am/is/are','do/does','did','done'] , 'correcta': 0},
    {'preguntas':'¿Forma "Pythonic" de iterar?','opciones':['for i in range','list comprehension','while true','do while'] , 'correcta': 1},
    {'preguntas':'¿Objeto base en Java?','opciones':['String','Integer','Object','Main'] , 'correcta': 2},
    {'preguntas':'¿Todo es un objeto en Python?','opciones':['Sí','No','Solo clases','Solo funciones'] , 'correcta': 0},
    {'preguntas':'¿Sistemas operativos libres?','opciones':['Windows','macOS','Linux','iOS'] , 'correcta': 2},
    {'preguntas':'¿Lenguaje de marcas?','opciones':['Java','Python','HTML','C++'] , 'correcta': 2},
    {'preguntas':'¿Desarrollo de aplicaciones?','opciones':['Frontend','Backend','Fullstack','Todas las anteriores'] , 'correcta': 3},
    {'preguntas':'¿Creador del Bitcoin?','opciones':['Elon Musk','Satoshi Nakamoto','Bill Gates','Steve Jobs'] , 'correcta': 1},
]
#1.Barajamo las preguntas antes de empezar
random.shuffle(preguntas)
#2.variables de control
historial_resultados = [] #para el resuemne detallado final
contador_aciertos = 0 

#3.bucle principal (recorremos la lista barajada una sola vez)

for idx, p in enumerate (preguntas , 1 ):
    solucion_correcta = mostrar_pregunta(p,idx)

    #validacion de entrada
    eleccion_usuario = 0 
    while eleccion_usuario not in[1,2,3,4]:
        try:
            eleccion_usuario = int(input("Introduce tu respueesta 1-4 "))
            if eleccion_usuario  not in [1,2,3,4]:
                print("Por favor , elegie un numero del 1 al 4")
        except ValueError:
            print("Entrada no valida debe ser un numero ")
    #verificacion
    es_correcto = (eleccion_usuario == solucion_correcta )

    if es_correcto:
        contador_aciertos += 1  
        print("Respuesta correcta")
    else:
        print(f"Incorrecta la respuesta era la {solucion_correcta}")

    #guardamos en el historial para el resumen final

    historial_resultados.append(
        {
            'pregunta':p['preguntas'],
            'resultado':"Correcto" if es_correcto else "Fallo",
            'tu_eleccion':p['opciones'][eleccion_usuario-1]
        }
    )

#estadisticas finales ---
print("\n" + "*"*40)
print(f"{'RESUMEN DEL EXAMEN':^40}")
print("*"*40)

for item in historial_resultados:
    print(f"[{item['resultado']}] {item['pregunta']} -> Elegiste: {item['tu_eleccion']}")

print("-"*40)
print(f"ACIERTOS: {contador_aciertos} | FALLOS : {8- contador_aciertos}")

if Aprobado_Suspendido(contador_aciertos):
    print("ESTADO FINAL: !APROBADO! ")
else:
    print("ESTADO FINAL : SUSPENDIDO")
    print("Debes repasar las preguntas falladas ")
    