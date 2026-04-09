from datetime import datetime

class Historial:
    def __init__(self):
        self.acciones = []
    
    def registrar(self, accion, fecha=None):
        self.acciones.append({
            "accion": accion,
            "fecha": fecha or datetime.now()
        })
    
    def buscar(self, texto):
        return [a for a in self.acciones if texto.lower() in a["accion"].lower()]
    
    def __str__(self):
        return "\n".join(
            f"{a['fecha'].strftime('%Y-%m-%d %H:%M')} - {a['accion']}" 
            for a in self.acciones
        )

h = Historial()
h.registrar("Iniciar sesión")
h.registrar("Comprar espada")
h.registrar("Nivel subido")
h.registrar("Completar misión")

print("=== Historial ===")
print(h)

print("\n=== Buscar 'comprar' ===")
for a in h.buscar("comprar"):
    print(a["accion"])
