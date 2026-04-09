from datetime import datetime, timedelta

class Pista:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.ocupada = False

class Reserva:
    def __init__(self, pista, nombre, hora_inicio, duracion_horas):
        self.pista = pista
        self.nombre = nombre
        self.hora_inicio = hora_inicio
        self.duracion = duracion_horas
    
    @property
    def hora_fin(self):
        return self.hora_inicio + timedelta(hours=self.duracion)

class ClubPadel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pistas = [Pista(i, "cristal" if i%2==0 else "pared") for i in range(1, 5)]
        self.reservas = []
    
    def buscar_pista_libre(self, hora, duracion):
        for pista in self.pistas:
            if not pista.ocupada:
                return pista
        return None
    
    def crear_reserva(self, nombre, hora, duracion):
        pista = self.buscar_pista_libre(hora, duracion)
        if pista:
            pista.ocupada = True
            res = Reserva(pista, nombre, hora, duracion)
            self.reservas.append(res)
            print(f"Reservado: {pista.numero} para {nombre}")
        else:
            print("No hay pistas disponibles")

club = ClubPadel("SportPadel")
hora = datetime.now()
club.crear_reserva("Juan", hora, 2)
club.crear_reserva("Maria", hora, 1)
print(f"Pistas libres: {sum(1 for p in club.pistas if not p.ocupada)}")
