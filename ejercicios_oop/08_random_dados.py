class Dado:
    def __init__(self, caras=6):
        self.caras = caras
        self.valor = 1
    
    def lanzar(self):
        import random
        self.valor = random.randint(1, self.caras)
        return self.valor

class JuegoDados:
    def __init__(self):
        self.dados = [Dado(6), Dado(6), Dado(6)]
    
    def jugar(self):
        resultados = [d.lanzar() for d in self.dados]
        print(f"Resultados: {resultados}")
        print(f"Total: {sum(resultados)}")
        
        if resultados == [6, 6, 6]:
            print("¡JACKPOT!")
        elif resultados[0] == resultados[1] == resultados[2]:
            print("¡Triple!")
        elif resultados[0] == resultados[1] or resultados[1] == resultados[2]:
            print("¡Doble!")
        
        return resultados

juego = JuegoDados()
for _ in range(5):
    juego.jugar()
    print("-" * 20)
