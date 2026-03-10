# EJERCICIO: Sistema de Gestión de Vehículos
## Conceptos: Herencia, Polimorfismo y ArrayList

---

## 📋 DESCRIPCIÓN DEL EJERCICIO

Este ejercicio implementa un **sistema de gestión de vehículos** que demuestra los conceptos de:
- **Herencia**: Clases que heredan de una clase base
- **Polimorfismo**: Métodos que se comportan diferente según el tipo de objeto
- **ArrayList**: Colección para almacenar objetos de diferentes tipos

---

## 📁 ESTRUCTURA DEL PROYECTO

```
Ejercicio5/
├── Vehiculo.java          (Clase base/padre)
├── Coche.java             (Hereda de Vehiculo)
├── Moto.java              (Hereda de Vehiculo)
├── Camion.java            (Hereda de Vehiculo)
├── GestorVehiculos.java   (Gestiona ArrayList de vehículos)
└── MainVehiculos.java     (Programa principal)
```

---

## 🔑 CONCEPTOS CLAVE

### 1️⃣ HERENCIA

La clase `Vehiculo` es la **clase padre** (superclase) que define:
- **Atributos comunes**: marca, modelo, año, precio
- **Métodos base**: mostrarInfo(), calcularImpuesto(), getters/setters

Las clases `Coche`, `Moto` y `Camión` **heredan** de `Vehiculo`:
```java
public class Coche extends Vehiculo {
    // Hereda todos los atributos y métodos de Vehiculo
    // Añade sus propios atributos: numPuertas, tipoCombustible
}
```

**Beneficios:**
- Reutilización de código
- Jerarquía clara de clases
- Mantenimiento más fácil

---

### 2️⃣ POLIMORFISMO

El mismo método se ejecuta diferente según el tipo de objeto.

**Ejemplo: Método `mostrarInfo()`**
```java
Vehiculo v1 = new Coche(...);
Vehiculo v2 = new Moto(...);
Vehiculo v3 = new Camion(...);

v1.mostrarInfo(); // Ejecuta mostrarInfo de Coche
v2.mostrarInfo(); // Ejecuta mostrarInfo de Moto
v3.mostrarInfo(); // Ejecuta mostrarInfo de Camion
```

**Ejemplo: Método `calcularImpuesto()`**
- Coches: 12% del precio
- Motos: 8% del precio
- Camiones: 15% del precio

Cada clase sobrescribe (`@Override`) el método con su propia implementación.

---

### 3️⃣ ARRAYLIST

El `GestorVehiculos` usa un `ArrayList` para almacenar vehículos de diferentes tipos:

```java
private ArrayList<Vehiculo> vehiculos;

public void agregarVehiculo(Vehiculo v) {
    vehiculos.add(v); // Puede ser Coche, Moto o Camion
}

public void mostrarTodosLosVehiculos() {
    for (Vehiculo v : vehiculos) {
        v.mostrarInfo(); // Polimorfismo en acción
    }
}
```

**Ventajas:**
- Almacena cualquier tipo de Vehiculo
- Tamaño dinámico (crece automáticamente)
- Acceso fácil a los elementos

---

## 🎯 CARACTERÍSTICAS DEL EJERCICIO

### Métodos de `GestorVehiculos`:

1. **agregarVehiculo(Vehiculo v)**
   - Agrega cualquier tipo de vehículo al ArrayList

2. **mostrarTodosLosVehiculos()**
   - Muestra todos los vehículos (demuestra POLIMORFISMO)

3. **mostrarImpuestos()**
   - Calcula y muestra el impuesto de cada vehículo (POLIMORFISMO)

4. **buscarPorMarca(String marca)**
   - Retorna ArrayList con vehículos de una marca específica

5. **contarVehiculosPorTipo()**
   - Usa `instanceof` para contar cada tipo de vehículo

6. **mostrarVehiculoMasCaro()**
   - Busca el vehículo con mayor precio

7. **eliminarVehiculo(int indice)**
   - Elimina un vehículo del ArrayList

---

## 🔬 CONCEPTOS AVANZADOS

### Sobrescritura (Override)
Cada clase hija implementa `mostrarInfo()` y `calcularImpuesto()` de forma diferente:

```java
// En Coche
@Override
public double calcularImpuesto() {
    return precio * 0.12; // 12%
}

// En Moto
@Override
public double calcularImpuesto() {
    return precio * 0.08; // 8%
}
```

### Casting (Conversión de tipos)
Cuando necesitas acceder a métodos específicos, usas casting:

```java
if (vehiculo instanceof Coche) {
    ((Coche) vehiculo).abrirMaletero();
}
```

### Uso de `super`
Llama al constructor de la clase padre:

```java
public Coche(String marca, String modelo, int año, double precio, ...) {
    super(marca, modelo, año, precio); // Llama al constructor de Vehiculo
    this.numPuertas = numPuertas;
}
```

---

## ▶️ CÓMO EJECUTAR

1. Compila todos los archivos:
   ```bash
   javac Vehiculo.java
   javac Coche.java
   javac Moto.java
   javac Camion.java
   javac GestorVehiculos.java
   javac MainVehiculos.java
   ```

2. Ejecuta el programa:
   ```bash
   java MainVehiculos
   ```

---

## 📊 EJEMPLO DE SALIDA

```
===== SISTEMA DE GESTIÓN DE VEHÍCULOS =====

[Vehículo 1]
=== COCHE ===
Marca: Toyota, Modelo: Corolla
Año: 2023, Precio: $25000
Puertas: 4, Combustible: Gasolina

[Vehículo 2]
=== MOTO ===
Marca: Yamaha, Modelo: R6
Año: 2023, Precio: $8000
Cilindrada: 600cc, Refugio: Sí

[Vehículo 3]
=== CAMIÓN ===
Marca: Volvo, Modelo: FH
Año: 2023, Precio: $80000
Capacidad de carga: 25 toneladas, Ejes: 3
```

---

## 📚 EJERCICIOS PROPUESTOS

1. **Agregar nueva clase**: Crea una clase `Bicicleta` que herede de `Vehiculo`
2. **Nuevo método**: Agreguen un método `acelerar()` que imprima mensajes según el tipo
3. **Ordenamiento**: Ordena los vehículos por precio
4. **Filtrado**: Crea un método que retorne solo los vehículos posteriores a año 2023
5. **Persistencia**: Guarda la lista de vehículos en un archivo
6. **Interfaz gráfica**: Crea un menú interactivo en consola

---

## 🎓 CONCEPTOS REFORZADOS

✅ Herencia (`extends`)
✅ Polimorfismo (métodos sobrescritos)
✅ ArrayList (colección genérica)
✅ Casting (`instanceof` y conversión de tipos)
✅ Encapsulación (atributos protected y private)
✅ Getters y setters
✅ Métodos static vs instance
✅ Bucles y estructuras de control

---

## 💡 TIPS IMPORTANTES

- La clase `Vehiculo` es la base común
- Cada clase hija especializa el comportamiento
- El ArrayList almacena referencias a `Vehiculo`
- Se puede polimorfismo de forma transparente
- Usa `instanceof` para verificar tipos
- Aprende a diseñar jerarquías de clases

---

¡Ahora tienes un ejercicio completo sobre herencia, polimorfismo y ArrayList! 🚀
