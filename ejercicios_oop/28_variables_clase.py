class Robot:
    contador = 0
    
    def __init__(self, nombre):
        self.nombre = nombre
        Robot.contador += 1
        self.id = Robot.contador
    
    def __del__(self):
        Robot.contador -= 1
        print(f"Robot {self.id} eliminado")

r1 = Robot("R2D2")
r2 = Robot("C3PO")
r3 = Robot("BB8")

print(f"Total robots: {Robot.contador}")
del r2
print(f"Total robots después de eliminar: {Robot.contador}")
