class Tareas:
    diccionario_tareas = {}  # Diccionario de clase (compartido)
    
    def __init__(self, identificador, titulo, prioridad):
        # Verificar si el ID ya existe ANTES de crear
        if identificador in Tareas.diccionario_tareas:
            print(f"Error: ID {identificador} ya existente")
            return
        
        # Validar prioridad
        if prioridad < 1 or prioridad > 9:
            print("Error: La prioridad debe estar entre 1 y 9")
            return
        
        # Asignar directamente (el setter no se usa en __init__)
        self._identificador = identificador
        self._titulo = titulo
        self._prioridad = prioridad
        self._estado = False  # No completada por defecto
        
        # Añadir al diccionario
        Tareas.diccionario_tareas[identificador] = {
            'identificador': self._identificador,
            'titulo': self._titulo,
            'prioridad': self._prioridad,
            'estado_tarea': self._estado
        }
        
        print(f"Tarea '{titulo}' (ID: {identificador}) añadida.")
    
    @property
    def identificador(self):
        return self._identificador
    
    @identificador.setter
    def identificador(self, nuevo_valor):
        # Verificar si el nuevo ID ya existe
        if nuevo_valor in Tareas.diccionario_tareas:
            print(f"Error: ID {nuevo_valor} ya existente")
            return
        self._identificador = nuevo_valor
    
    def eliminarTarea(self, identificador):
        if identificador in Tareas.diccionario_tareas:
            titulo = Tareas.diccionario_tareas[identificador]['titulo']
            del Tareas.diccionario_tareas[identificador]
            print(f"Tarea con ID {identificador} ('{titulo}') eliminada.")
        else:
            print(f"Error: No se encontró una tarea con ID {identificador}.")
    
    def marcarComoCompletada(self, identificador):
        if identificador in Tareas.diccionario_tareas:
            Tareas.diccionario_tareas[identificador]['estado_tarea'] = True
            titulo = Tareas.diccionario_tareas[identificador]['titulo']
            print(f"Tarea ID {identificador} '{titulo}' marcada como completada.")
        else:
            print(f"Error: No se encontró una tarea con ID {identificador}.")
    
    def mostrarTareasCompletadas(self):
        print("- LISTADO DE TAREAS:")
        completadas = [t for t in Tareas.diccionario_tareas.values() if t['estado_tarea']]
        if not completadas:
            print("No hay tareas completadas.")
        else:
            for tarea in completadas:
                print(f"[{tarea['identificador']}] {tarea['titulo']} (Prioridad: {tarea['prioridad']})")
    
    def mostrarTareasNoCompletadas(self):
        print("- LISTADO DE TAREAS:")
        no_completadas = [t for t in Tareas.diccionario_tareas.values() if not t['estado_tarea']]
        if not no_completadas:
            print("No hay tareas no completadas.")
        else:
            for tarea in no_completadas:
                print(f"[{tarea['identificador']}] {tarea['titulo']} (Prioridad: {tarea['prioridad']})")


# Ejemplo de uso
t1 = Tareas("P10", "Comprar billetes", 5)
t2 = Tareas("E25", "Enviar email al jefe", 5)
t3 = Tareas("P33", "Aprender Python", 2)
t4 = Tareas("P10", "Otra tarea", 3)  # Error: ID duplicado

print("\n--- Tareas no completadas ---")
t2.mostrarTareasNoCompletadas()

print("\n--- Marcar como completada ---")
t1.marcarComoCompletada("P10")

print("\n--- Tareas completadas ---")
t1.mostrarTareasCompletadas()

print("\n--- Eliminar tarea ---")
t1.eliminarTarea("E25")

print("\n--- Tareas no completadas (después de eliminar) ---")
t1.mostrarTareasNoCompletadas()
