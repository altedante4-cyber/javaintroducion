from abc import ABC, abstractmethod

class EstadoJuego(ABC):
    @abstractmethod
    def ejecutar(self, juego):
        pass

class MenuPrincipal(EstadoJuego):
    def ejecutar(self, juego):
        print("=== MENÚ PRINCIPAL ===")
        print("1. Nueva Partida")
        print("2. Continuar")
        print("3. Salir")
        print("-> Seleccionado: Nueva Partida")
        return "Jugando"

class Jugando(EstadoJuego):
    def ejecutar(self, juego):
        print("=== JUGANDO ===")
        print("Misión: Derrotar al dragón")
        print("¡Victoria! Volviendo al menú...")
        return "MenuPrincipal"

class Juego:
    def __init__(self):
        self.estados = {
            "MenuPrincipal": MenuPrincipal(),
            "Jugando": Jugando()
        }
        self.estado_actual = "MenuPrincipal"
    
    def ejecutar(self):
        estado = self.estados[self.estado_actual]
        self.estado_actual = estado.ejuego(self)

juego = Juego()
for _ in range(3):
    juego.ejecutar()
    print("-" * 20)
