import random

class Question:
    def __init__(self, pregunta, opciones, respuesta_correcta):
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta
    
    def verificar(self, respuesta):
        return respuesta == self.respuesta_correcta
    
    def __str__(self):
        opts = "\n".join(f"{i+1}. {o}" for i, o in enumerate(self.opciones))
        return f"{self.pregunta}\n{opts}"

class Trivia:
    def __init__(self, titulo):
        self.titulo = titulo
        self.preguntas = []
    
    def agregar_pregunta(self, pregunta, opciones, respuesta):
        self.preguntas.append(Question(pregunta, opciones, respuesta))
    
    def jugar(self):
        random.shuffle(self.preguntas)
        aciertos = 0
        for p in self.preguntas:
            print(f"\n{p}")
            try:
                resp = int(input("Respuesta: ")) - 1
                if p.verificar(resp):
                    print("¡Correcto!")
                    aciertos += 1
                else:
                    print("Incorrecto")
            except:
                print("Entrada inválida")
        print(f"\n=== Resultado: {aciertos}/{len(self.preguntas)} ===")

t = Trivia("Trivia de Videojuegos")
t.agregar_pregunta("¿Cuántos juegos de Zelda existen?", ["20", "35", "45"], 1)
t.agregar_pregunta("¿Quién creó Mario?", ["Miyamoto", "Pescatori", "Uemura"], 0)
t.agregar_pregunta("¿Año de lanzamiento de DOOM?", ["1991", "1993", "1995"], 1)
t.jugar()
