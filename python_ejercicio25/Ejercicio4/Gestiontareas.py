class Tareas:

    dicionario_tareas ={}
    def __init__(self,identificador:str,titulo:str , prioridad:int ):

        if identificador in Tareas.dicionario_tareas:
             print(f"Error: {identificador} ya existente")
             return
        
        self._identificador = identificador
        self._titulo = titulo

        if prioridad >= 1 and prioridad <= 9 :
             self._prioridad = prioridad
        else:
            self._prioridad = 0 

        self._estado = False #no completada 

        Tareas.dicionario_tareas[identificador]= {
             'identificador': self._identificador,
             'titulo':titulo,
             'prioridad':prioridad,
             'estado_tarea':self._estado
        }    

    
    @property
    def identificador(self):
        return self._identificador
        
    @identificador.setter
    def identificador(self,nuevo_valor):
        if nuevo_valor in Tareas.dicionario_tareas:
            return 

        self._identificador = nuevo_valor          
         
    
    def eliminarTarea(self,identificador):

        if identificador in Tareas.dicionario_tareas:
            print(f"Tarea con {identificador} ({Tareas.dicionario_tareas[identificador]['titulo']}) eliminada")
            del Tareas.dicionario_tareas[identificador]
            return
        else:
            print("No se encontro una tarea con ID X1005")

    def marcarComoCOmpletada(self,identificador):

        if identificador in Tareas.dicionario_tareas:
            print(f"Tarea con {identificador} ({Tareas.dicionario_tareas[identificador]['titulo']}) marcada como completada")
            Tareas.dicionario_tareas[identificador]['estado_tarea']=True
            return
        else:
            print(f"No se encontro una tarea con {identificador}")
    
    
    def mostrarTareasCompletadas(self):

            if not Tareas.dicionario_tareas:
                print("LISTADO DE TAREAS ")
                print("No hay contenido en el dicionario")
            
            if any(x['estado_tarea'] for x in Tareas.dicionario_tareas.values() ):


                print("LISTADO DE TAREAS")
                for i in Tareas.dicionario_tareas.values():

                    if i['estado_tarea']:
                        print(f"[{i['identificador']}] {i['titulo']}  (Prioridad: {i['prioridad']})")

            else:
                print("LISTADO DE TAREAS")
                print("No hay tareas completadas")

    def mostrarTareasNoCompletadas(self):

        if not Tareas.dicionario_tareas:
            print("LISTADO DE TAREAS")
            print("No hay contenido en el diccionario")
            return
        
        no_completadas = [t for t in Tareas.dicionario_tareas.values() if not t['estado_tarea']]
        
        if no_completadas:
            print("LISTADO DE TAREAS")
            for i in no_completadas:
                print(f"[{i['identificador']}] {i['titulo']}  (Prioridad: {i['prioridad']})")
        else:
            print("LISTADO DE TAREAS")
            print("No hay tareas no completadas")


# PRUEBAS   
print("=== CREAR TAREAS ===")
t1 = Tareas("P10", "Comprar billetes", 5)
t2 = Tareas("E25", "Enviar email al jefe", 5)
t3 = Tareas("P33", "Aprender Python", 2)
t4 = Tareas("F47", "Revisar facturas", 7)
# ID duplicado
print("\n=== ID DUPLICADO ===")
t5 = Tareas("P10", "Otra tarea", 3)

t1.mostrarTareasCompletadas()
t2.mostrarTareasNoCompletadas()
