class MaquinaExpresos:
    def __init__(self):
        self.bebidas = []
        self.cantidad = 0
    
    def __call__(self, tipo):
        self.cantidad += 1
        nombre = f"Café {tipo} #{self.cantidad}"
        self.bebidas.append(nombre)
        return nombre

maquina = MaquinaExpresos()
print(maquina("expreso"))
print(maquina("latte"))
print(maquina("capuchino"))
print(f"Total bebidas: {len(maquina.bebidas)}")
