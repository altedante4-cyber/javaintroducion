# Clases Abstractas en Python - Guía Completa

## 📚 Introducción

Hola, te presento una guía comprensiva sobre **clases abstractas** en Python. Como tu mentor senior, te mostrearé por qué son importantes, cómo usarlas y las mejores prácticas en desarrollo profesional.

Las clases abstractas son un concepto fundamental en la **Programación Orientada a Objetos (POO)** que te permite definir contratos que las subclases deben cumplir.

---

## 🎯 ¿Qué es una Clase Abstracta?

Una **clase abstracta** es una clase que no puede ser instanciada directamente. Su propósito es servir como una plantilla o interfaz que define qué métodos deben implementar sus subclases.

### Características principales:

- ✅ No se pueden crear instancias directamente
- ✅ Define la estructura que deben seguir las subclases
- ✅ Establece un contrato entre la clase padre y sus hijos
- ✅ Mejora la mantenibilidad y organización del código
- ✅ Facilita el polimorfismo

---

## 📦 Módulo `abc` - Abstract Base Classes

Python proporciona el módulo `abc` (Abstract Base Classes) para trabajar con clases abstractas.

### Requisitos básicos:

```python
from abc import ABC, abstractmethod
```

- **ABC**: Clase base para definir clases abstractas
- **@abstractmethod**: Decorador que marca un método como abstracto

---

## 💡 Ejemplo 1: Concepto Básico

Imagina que eres una empresa que desarrolla diferentes tipos de vehículos. Quieres asegurar que todos los vehículos tengan ciertos métodos.

```python
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    """Clase abstracta que define la interfaz para todos los vehículos"""
    
    @abstractmethod
    def acelerar(self):
        """Todo vehículo debe poder acelerar"""
        pass
    
    @abstractmethod
    def frenar(self):
        """Todo vehículo debe poder frenar"""
        pass
    
    @abstractmethod
    def obtener_velocidad_maxima(self):
        """Todo vehículo debe retornar su velocidad máxima"""
        pass


# ❌ ESTO CAUSARÁ ERROR - No puedes instanciar una clase abstracta
# auto = Vehiculo()  # TypeError: Can't instantiate abstract class Vehiculo

# ✅ Crear una subclase que implemente los métodos abstractos
class Auto(Vehiculo):
    def __init__(self, marca, velocidad_maxima):
        self.marca = marca
        self.velocidad_actual = 0
        self._velocidad_maxima = velocidad_maxima
    
    def acelerar(self):
        if self.velocidad_actual < self._velocidad_maxima:
            self.velocidad_actual += 20
            print(f"{self.marca} aceleró a {self.velocidad_actual} km/h")
    
    def frenar(self):
        if self.velocidad_actual > 0:
            self.velocidad_actual -= 15
            print(f"{self.marca} frenó a {self.velocidad_actual} km/h")
    
    def obtener_velocidad_maxima(self):
        return self._velocidad_maxima


# ✅ Ahora sí puedes crear instancias
mi_auto = Auto("Toyota", 180)
mi_auto.acelerar()        # Toyota aceleró a 20 km/h
mi_auto.acelerar()        # Toyota aceleró a 40 km/h
mi_auto.frenar()          # Toyota frenó a 25 km/h
print(f"Velocidad máxima: {mi_auto.obtener_velocidad_maxima()} km/h")
```

---

## 💡 Ejemplo 2: Jerarquía de Clases

Veamos un ejemplo más realista con múltiples niveles de abstracción:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    """Clase abstracta base para todos los animales"""
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    @abstractmethod
    def hacer_sonido(self):
        pass
    
    @abstractmethod
    def moverse(self):
        pass
    
    # Método concreto (no abstracto) - todas las subclases lo heredan
    def envejecer(self):
        self.edad += 1
        print(f"{self.nombre} ahora tiene {self.edad} años")


class Perro(Animal):
    """Implementación concreta de Animal"""
    
    def hacer_sonido(self):
        return "¡Guau guau!"
    
    def moverse(self):
        return "Correr con las 4 patas"


class Pajaro(Animal):
    """Otra implementación concreta de Animal"""
    
    def hacer_sonido(self):
        return "¡Pío pío!"
    
    def moverse(self):
        return "Volar"


# Uso
perro = Perro("Rex", 3)
pajaro = Pajaro("Tweety", 1)

print(perro.hacer_sonido())      # ¡Guau guau!
print(pajaro.hacer_sonido())     # ¡Pío pío!

perro.envejecer()                # Rex ahora tiene 4 años
pajaro.moverse()                 # Volar
```

---

## 💡 Ejemplo 3: Métodos Abstractos con Implementación

A veces una clase abstracta proporciona una implementación base que las subclases pueden extender usando `super()`:

```python
from abc import ABC, abstractmethod

class Empleado(ABC):
    """Clase abstracta para empleados"""
    
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    @abstractmethod
    def calcular_bono(self):
        """Método abstracto con implementación base"""
        # Todas las subclases pueden usar esta lógica base
        return self.salario * 0.05  # 5% de bono base
    
    def obtener_info(self):
        """Método concreto disponible para todas las subclases"""
        return f"Empleado: {self.nombre}, Salario: ${self.salario}"


class Programador(Empleado):
    def calcular_bono(self):
        # Usa la implementación base y la extiende
        bono_base = super().calcular_bono()
        bono_especial = self.salario * 0.10  # 10% adicional para programadores
        return bono_base + bono_especial


class Gerente(Empleado):
    def calcular_bono(self):
        # Implementación diferente para gerentes
        return self.salario * 0.20  # 20% de bono


# Uso
prog = Programador("Juan", 3000)
print(prog.obtener_info())           # Empleado: Juan, Salario: $3000
print(f"Bono: ${prog.calcular_bono()}")  # Bono: $450

gerente = Gerente("María", 5000)
print(gerente.obtener_info())        # Empleado: María, Salario: $5000
print(f"Bono: ${gerente.calcular_bono()}")  # Bono: $1000
```

---

## 💡 Ejemplo 4: Propiedades Abstractas

También puedes definir propiedades abstractas usando `@property` y `@abstractmethod`:

```python
from abc import ABC, abstractmethod

class Cuenta(ABC):
    """Clase abstracta para cuentas bancarias"""
    
    @property
    @abstractmethod
    def saldo(self):
        """La subclase debe proporcionar una forma de obtener el saldo"""
        pass
    
    @abstractmethod
    def depositar(self, cantidad):
        pass
    
    @abstractmethod
    def retirar(self, cantidad):
        pass


class CuentaAhorros(Cuenta):
    def __init__(self, titular):
        self.titular = titular
        self._saldo = 0.0
        self.interes = 0.03  # 3% anual
    
    @property
    def saldo(self):
        return self._saldo
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito confirmado: ${cantidad}. Saldo: ${self._saldo}")
    
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"Retiro confirmado: ${cantidad}. Saldo: ${self._saldo}")
        else:
            print("Retiro rechazado")
    
    def aplicar_interes(self):
        self._saldo *= (1 + self.interes)
        print(f"Interés aplicado. Nuevo saldo: ${self._saldo:.2f}")


# Uso
cuenta = CuentaAhorros("Carlos")
cuenta.depositar(1000)      # Depósito confirmado: $1000. Saldo: $1000.0
cuenta.depositar(500)       # Depósito confirmado: $500. Saldo: $1500.0
cuenta.aplicar_interes()    # Interés aplicado. Nuevo saldo: $1545.00
cuenta.retirar(200)         # Retiro confirmado: $200. Saldo: $1345.0
```

---

## ⚠️ Ejemplo 5: Errores Comunes

Veamos qué sucede cuando NO implementas todos los métodos abstractos:

```python
from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def saludar(self):
        pass
    
    @abstractmethod
    def presentarse(self):
        pass


# ❌ ESTO CAUSARÁ ERROR - No implementa presentarse()
class Estudiante(Persona):
    def saludar(self):
        return "¡Hola!"
    # Falta implementar presentarse()


# TypeError: Can't instantiate abstract class Estudiante with abstract method presentarse
# estudiante = Estudiante()

# ✅ SOLUCIÓN - Implementar todos los métodos abstractos
class EstudianteCompleto(Persona):
    def saludar(self):
        return "¡Hola!"
    
    def presentarse(self):
        return "Soy un estudiante"


estudiante = EstudianteCompleto()
print(estudiante.saludar())        # ¡Hola!
print(estudiante.presentarse())   # Soy un estudiante
```

---

## 🎓 Caso de Uso Real: Sistema de Pagos

Veamos cómo las clases abstractas son útiles en un proyecto real:

```python
from abc import ABC, abstractmethod
from datetime import datetime

class MetodoPago(ABC):
    """Interfaz para diferentes métodos de pago"""
    
    @abstractmethod
    def procesar_pago(self, monto):
        pass
    
    @abstractmethod
    def verificar_saldo(self):
        pass
    
    def registrar_transaccion(self, monto):
        """Método común para todos los métodos de pago"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Transacción registrada: ${monto}")


class TarjetaCredito(MetodoPago):
    def __init__(self, numero, limite):
        self.numero = numero
        self.limite = limite
        self.saldo_usado = 0.0
    
    def procesar_pago(self, monto):
        if self.saldo_usado + monto <= self.limite:
            self.saldo_usado += monto
            self.registrar_transaccion(monto)
            print(f"Pago con tarjeta aprobado. Usado: ${self.saldo_usado}")
            return True
        else:
            print("Límite de crédito excedido")
            return False
    
    def verificar_saldo(self):
        return self.limite - self.saldo_usado


class Transferencia(MetodoPago):
    def __init__(self, saldo_cuenta):
        self.saldo_cuenta = saldo_cuenta
    
    def procesar_pago(self, monto):
        if monto <= self.saldo_cuenta:
            self.saldo_cuenta -= monto
            self.registrar_transaccion(monto)
            print(f"Transferencia completada. Saldo restante: ${self.saldo_cuenta}")
            return True
        else:
            print("Fondos insuficientes")
            return False
    
    def verificar_saldo(self):
        return self.saldo_cuenta


class Bitcoin(MetodoPago):
    def __init__(self, saldo_btc):
        self.saldo_btc = saldo_btc
    
    def procesar_pago(self, monto_usd):
        tasa_conversion = 40000  # 1 BTC = $40,000 USD
        cantidad_btc = monto_usd / tasa_conversion
        
        if cantidad_btc <= self.saldo_btc:
            self.saldo_btc -= cantidad_btc
            self.registrar_transaccion(monto_usd)
            print(f"Pago en Bitcoin confirmado. Saldo: {self.saldo_btc:.6f} BTC")
            return True
        else:
            print("Bitcoin insuficiente")
            return False
    
    def verificar_saldo(self):
        return self.saldo_btc


# Función que funciona con CUALQUIER método de pago
def realizar_compra(metodo_pago, monto):
    """Esta función es flexible gracias a las clases abstractas"""
    print(f"\n--- Procesando compra de ${monto} ---")
    if metodo_pago.procesar_pago(monto):
        print("✅ Compra exitosa")
        print(f"Saldo disponible: {metodo_pago.verificar_saldo()}")
    else:
        print("❌ Compra rechazada")


# Uso
tarjeta = TarjetaCredito("1234567890", 5000)
realizar_compra(tarjeta, 500)
realizar_compra(tarjeta, 4800)  # Excede límite

transferencia = Transferencia(2000)
realizar_compra(transferencia, 500)

bitcoin = Bitcoin(0.05)
realizar_compra(bitcoin, 200)
```

---

## 🏆 Ventajas de las Clases Abstractas

| Ventaja | Explicación |
|---------|------------|
| **Contrato claro** | Define qué métodos DEBE implementar cada subclase |
| **Polimorfismo** | Código que funciona con diferentes tipos |
| **Mantenibilidad** | Más fácil de entender y modificar en el futuro |
| **Prevenir errores** | Se detec tan en tiempo de desarrollo, no en producción |
| **Reutilización** | Código común puede estar en la clase abstracta |
| **Documentación viva** | La clase abstracta documenta la interfaz esperada |

---

## 🚀 Mejores Prácticas

### 1. Nombres descriptivos
```python
# ✅ Bueno
class BaseDatos(ABC):
    pass

# ❌ Evitar
class X(ABC):
    pass
```

### 2. Documentación clara
```python
class Procesador(ABC):
    @abstractmethod
    def procesar(self, datos):
        """
        Procesa los datos de entrada.
        
        Args:
            datos: Los datos a procesar
            
        Returns:
            Resultado procesado
        """
        pass
```

### 3. Usar tipos (Type Hints)
```python
from abc import ABC, abstractmethod
from typing import List, Dict

class Analizador(ABC):
    @abstractmethod
    def analizar(self, texto: str) -> Dict[str, int]:
        pass
```

### 4. No abusar de la abstracción
```python
# ❌ Demasiada abstracción
class Animal(ABC): pass
class Mamifero(Animal, ABC): pass
class Carnivoro(Mamifero, ABC): pass
class Gato(Carnivoro): pass

# ✅ Abstracción justa
class Animal(ABC): pass
class Gato(Animal): pass
```

---

## 📝 Reflexión Final

Las clases abstractas son una herramienta poderosa cuando:

- ✅ Tienes múltiples clases que comparten comportamiento similar
- ✅ Quieres asegurar que las subclases implementen ciertos métodos
- ✅ Trabajas en equipos grandes donde el contrato es importante
- ✅ Necesitas código mantenible y escalable

Úsalas sabiamente, pero no abuses. A veces una clase normal es suficiente.

---

**Durante 15 años de experiencia en desarrollo, he aprendido que las clases abstractas son fundamentales en proyectos profesionales. Úsalas para escribir código más robusto y mantenible.**

¡Sigue practicando! 🚀
