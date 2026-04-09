from abc import ABC, abstractmethod

class DecoradorArma(ABC):
    @abstractmethod
    def get_descripcion(self) -> str:
        pass
    
    @abstractmethod
    def get_dano(self) -> int:
        pass

class ArmaBase(DecoradorArma):
    def __init__(self):
        self._nombre = "Espada"
        self._dano = 10
    
    def get_descripcion(self):
        return self._nombre
    
    def get_dano(self):
        return self._dano

class EnchantFuego(DecoradorArma):
    def __init__(self, arma):
        self.arma = arma
    
    def get_descripcion(self):
        return self.arma.get_descripcion() + " + Fuego"
    
    def get_dano(self):
        return self.arma.get_dano() + 15

class EnchantHielo(DecoradorArma):
    def __init__(self, arma):
        self.arma = arma
    
    def get_descripcion(self):
        return self.arma.get_descripcion() + " + Hielo"
    
    def get_dano(self):
        return self.arma.get_dano() + 10

arma = ArmaBase()
print(f"{arma.get_descripcion()}: {arma.get_dano()} dmg")

arma = EnchantFuego(ArmaBase())
print(f"{arma.get_descripcion()}: {arma.get_dano()} dmg")

arma = EnchantHielo(EnchantFuego(ArmaBase()))
print(f"{arma.get_descripcion()}: {arma.get_dano()} dmg")
