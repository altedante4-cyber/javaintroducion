from datetime import datetime

class Registro:
    def __init__(self):
        self.registros = []
    
    def __lshift__(self, mensaje):
        self.registros.append((datetime.now(), mensaje))
        return self
    
    def __str__(self):
        return "\n".join(f"{t.strftime('%H:%M:%S')} - {m}" for t, m in self.registros)

log = Registro()
log << "Inicio del juego"
log << "Usuario conectado"
log << "Partida iniciada"

print(log)
