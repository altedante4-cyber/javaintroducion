# Ejercicios de Nivel Medio - Java (ArrayLists, HashSets, Herencia, Polimorfismo y Abstracto)

---

## Ejercicio 1: Sistema de Gestión de Empleados

### Enunciado

Desarrolla un sistema de gestión de empleados para una empresa. El sistema debe:

1. **Crear una clase abstracta `Empleado`** con:
   - Atributos: `id`, `nombre`, `departamento`, `salarioBase`
   - Método abstracto: `calcularSalarioFinal()`
   - Método concreto: `mostrarInfo()`

2. **Crear clases concretas descendientes**:
   - `EmpleadoTiempoCompleto`: Hereda de `Empleado`, suma un bono del 15% al salarioBase
   - `EmpleadoTiempoPartial`: Hereda de `Empleado`, suma un bono del 5% al salarioBase
   - `Gerente`: Hereda de `EmpleadoTiempoCompleto`, suma un bono adicional del 20% sobre el salarioBase

3. **Usar `ArrayList`** para almacenar todos los empleados de la empresa

4. **Usar `HashSet`** para almacenar los nombres de los departamentos sin repetición

5. **Implementar métodos**:
   - Crear empleados y agregarlos al ArrayList
   - Mostrar información de todos los empleados
   - Calcular salario promedio por departamento (usando polimorfismo)
   - Mostrar lista de departamentos únicos (usando HashSet)

### Solución - Archivo: `SistemaEmpleados.java`

```java
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

// Clase abstracta
abstract class Empleado {
    protected int id;
    protected String nombre;
    protected String departamento;
    protected double salarioBase;
    
    public Empleado(int id, String nombre, String departamento, double salarioBase) {
        this.id = id;
        this.nombre = nombre;
        this.departamento = departamento;
        this.salarioBase = salarioBase;
    }
    
    // Método abstracto
    abstract double calcularSalarioFinal();
    
    // Método concreto
    public void mostrarInfo() {
        System.out.println("ID: " + id + " | Nombre: " + nombre + " | Depto: " + departamento + 
                         " | Salario Final: $" + calcularSalarioFinal());
    }
    
    public int getId() { return id; }
    public String getNombre() { return nombre; }
    public String getDepartamento() { return departamento; }
    public double getSalarioBase() { return salarioBase; }
}

// Clase descendiente 1
class EmpleadoTiempoCompleto extends Empleado {
    public EmpleadoTiempoCompleto(int id, String nombre, String departamento, double salarioBase) {
        super(id, nombre, departamento, salarioBase);
    }
    
    @Override
    double calcularSalarioFinal() {
        return salarioBase * 1.15; // Bono 15%
    }
}

// Clase descendiente 2
class EmpleadoTiempoPartial extends Empleado {
    public EmpleadoTiempoPartial(int id, String nombre, String departamento, double salarioBase) {
        super(id, nombre, departamento, salarioBase);
    }
    
    @Override
    double calcularSalarioFinal() {
        return salarioBase * 1.05; // Bono 5%
    }
}

// Clase descendiente 3 (herencia múltiple de jerarquía)
class Gerente extends EmpleadoTiempoCompleto {
    public Gerente(int id, String nombre, String departamento, double salarioBase) {
        super(id, nombre, departamento, salarioBase);
    }
    
    @Override
    double calcularSalarioFinal() {
        return salarioBase * 1.15 * 1.20; // Bono 15% + 20% adicional
    }
}

// Clase principal
public class SistemaEmpleados {
    private ArrayList<Empleado> empleados;
    private HashSet<String> departamentos;
    
    public SistemaEmpleados() {
        empleados = new ArrayList<>();
        departamentos = new HashSet<>();
    }
    
    public void agregarEmpleado(Empleado emp) {
        empleados.add(emp);
        departamentos.add(emp.getDepartamento());
    }
    
    public void mostrarTodosEmpleados() {
        System.out.println("\n=== LISTA DE EMPLEADOS ===");
        for (Empleado emp : empleados) {
            emp.mostrarInfo();
        }
    }
    
    public void mostrarDepartamentos() {
        System.out.println("\n=== DEPARTAMENTOS ===");
        for (String depto : departamentos) {
            System.out.println("- " + depto);
        }
    }
    
    public double calcularSalarioPromedioPorDepartamento(String depto) {
        double suma = 0;
        int contador = 0;
        for (Empleado emp : empleados) {
            if (emp.getDepartamento().equals(depto)) {
                suma += emp.calcularSalarioFinal();
                contador++;
            }
        }
        return contador > 0 ? suma / contador : 0;
    }
    
    public void mostrarPromediosPorDepartamento() {
        System.out.println("\n=== SALARIOS PROMEDIO POR DEPARTAMENTO ===");
        for (String depto : departamentos) {
            double promedio = calcularSalarioPromedioPorDepartamento(depto);
            System.out.println(depto + ": $" + String.format("%.2f", promedio));
        }
    }
    
    public static void main(String[] args) {
        SistemaEmpleados sistema = new SistemaEmpleados();
        
        // Agregar empleados
        sistema.agregarEmpleado(new EmpleadoTiempoCompleto(1, "Juan", "IT", 3000));
        sistema.agregarEmpleado(new EmpleadoTiempoCompleto(2, "María", "IT", 3500));
        sistema.agregarEmpleado(new EmpleadoTiempoPartial(3, "Carlos", "Ventas", 2000));
        sistema.agregarEmpleado(new Gerente(4, "Ana", "IT", 5000));
        sistema.agregarEmpleado(new EmpleadoTiempoPartial(5, "Luis", "RH", 1800));
        sistema.agregarEmpleado(new Gerente(6, "Pedro", "Ventas", 4500));
        
        // Mostrar información
        sistema.mostrarTodosEmpleados();
        sistema.mostrarDepartamentos();
        sistema.mostrarPromediosPorDepartamento();
    }
}
```

### Salida Esperada

```
=== LISTA DE EMPLEADOS ===
ID: 1 | Nombre: Juan | Depto: IT | Salario Final: $3450.0
ID: 2 | Nombre: María | Depto: IT | Salario Final: $4025.0
ID: 3 | Nombre: Carlos | Depto: Ventas | Salario Final: $2100.0
ID: 4 | Nombre: Ana | Depto: IT | Salario Final: $11500.0
ID: 5 | Nombre: Luis | Depto: RH | Salario Final: $1890.0
ID: 6 | Nombre: Pedro | Depto: Ventas | Salario Final: $10350.0

=== DEPARTAMENTOS ===
- IT
- Ventas
- RH

=== SALARIOS PROMEDIO POR DEPARTAMENTO ===
IT: $6325.00
Ventas: $6225.00
RH: $1890.00
```

---

## Ejercicio 2: Sistema de Gestión de Vehículos

### Enunciado

Crea un sistema para una agencia de alquiler de vehículos. El sistema debe:

1. **Crear una clase abstracta `Vehiculo`** con:
   - Atributos: `placa`, `marca`, `modelo`, `tarifa_diaria`, `disponible`
   - Método abstracto: `calcularCostoAlquiler(int dias)`
   - Método concreto: `mostrarDetalles()`

2. **Crear clases concretas descendientes**:
   - `Auto`: Costo base = tarifa * días
   - `SUV`: Costo = tarifa * días + 50 (costo adicional)
   - `Camion`: Costo = tarifa * días + 100 + (100 * días) por carga de combustible
   - `Deportivo`: Costo = tarifa * días * 1.25 (recargo por aseguro)

3. **Usar `ArrayList`** para almacenar todos los vehículos disponibles

4. **Usar `HashSet`** para almacenar las marcas de vehículos sin repetición

5. **Implementar métodos**:
   - Calcular costo de alquiler con polimorfismo
   - Filtrar vehículos por disponibilidad
   - Mostrar todas las marcas únicas
   - Marcar vehículos como alquilados/disponibles

### Solución - Archivo: `SistemaAlquilerVehiculos.java`

```java
import java.util.ArrayList;
import java.util.HashSet;

// Clase abstracta
abstract class Vehiculo {
    protected String placa;
    protected String marca;
    protected String modelo;
    protected double tarifa_diaria;
    protected boolean disponible;
    
    public Vehiculo(String placa, String marca, String modelo, double tarifa_diaria) {
        this.placa = placa;
        this.marca = marca;
        this.modelo = modelo;
        this.tarifa_diaria = tarifa_diaria;
        this.disponible = true;
    }
    
    // Método abstracto - polimorfismo
    abstract double calcularCostoAlquiler(int dias);
    
    // Método concreto
    public void mostrarDetalles() {
        System.out.println("Placa: " + placa + " | Marca: " + marca + " | Modelo: " + modelo + 
                         " | Tarifa: $" + tarifa_diaria + "/día | Disponible: " + 
                         (disponible ? "SÍ" : "NO"));
    }
    
    public String getPlaca() { return placa; }
    public String getMarca() { return marca; }
    public boolean isDisponible() { return disponible; }
    public void setDisponible(boolean disponible) { this.disponible = disponible; }
}

// Clase Auto
class Auto extends Vehiculo {
    public Auto(String placa, String marca, String modelo, double tarifa_diaria) {
        super(placa, marca, modelo, tarifa_diaria);
    }
    
    @Override
    double calcularCostoAlquiler(int dias) {
        return tarifa_diaria * dias;
    }
}

// Clase SUV
class SUV extends Vehiculo {
    public SUV(String placa, String marca, String modelo, double tarifa_diaria) {
        super(placa, marca, modelo, tarifa_diaria);
    }
    
    @Override
    double calcularCostoAlquiler(int dias) {
        return (tarifa_diaria * dias) + 50;
    }
}

// Clase Camion
class Camion extends Vehiculo {
    public Camion(String placa, String marca, String modelo, double tarifa_diaria) {
        super(placa, marca, modelo, tarifa_diaria);
    }
    
    @Override
    double calcularCostoAlquiler(int dias) {
        return (tarifa_diaria * dias) + 100 + (100 * dias);
    }
}

// Clase Deportivo
class Deportivo extends Vehiculo {
    public Deportivo(String placa, String marca, String modelo, double tarifa_diaria) {
        super(placa, marca, modelo, tarifa_diaria);
    }
    
    @Override
    double calcularCostoAlquiler(int dias) {
        return (tarifa_diaria * dias) * 1.25;
    }
}

// Clase Principal
public class SistemaAlquilerVehiculos {
    private ArrayList<Vehiculo> vehiculos;
    private HashSet<String> marcas;
    
    public SistemaAlquilerVehiculos() {
        vehiculos = new ArrayList<>();
        marcas = new HashSet<>();
    }
    
    public void agregarVehiculo(Vehiculo vehiculo) {
        vehiculos.add(vehiculo);
        marcas.add(vehiculo.getMarca());
    }
    
    public void mostrarTodosVehiculos() {
        System.out.println("\n=== TODOS LOS VEHÍCULOS ===");
        for (Vehiculo v : vehiculos) {
            v.mostrarDetalles();
        }
    }
    
    public void mostrarVehiculosDisponibles() {
        System.out.println("\n=== VEHÍCULOS DISPONIBLES ===");
        for (Vehiculo v : vehiculos) {
            if (v.isDisponible()) {
                v.mostrarDetalles();
            }
        }
    }
    
    public void mostrarMarcas() {
        System.out.println("\n=== MARCAS DE VEHÍCULOS ===");
        for (String marca : marcas) {
            System.out.println("- " + marca);
        }
    }
    
    public void alquilarVehiculo(String placa, int dias) {
        for (Vehiculo v : vehiculos) {
            if (v.getPlaca().equals(placa)) {
                if (v.isDisponible()) {
                    double costo = v.calcularCostoAlquiler(dias);
                    v.setDisponible(false);
                    System.out.println("\n✓ Vehículo alquilado exitosamente");
                    System.out.println("Placa: " + placa + " | Días: " + dias + 
                                     " | Costo Total: $" + String.format("%.2f", costo));
                } else {
                    System.out.println("\n✗ El vehículo no está disponible");
                }
                return;
            }
        }
        System.out.println("\n✗ Vehículo no encontrado");
    }
    
    public void devolverVehiculo(String placa) {
        for (Vehiculo v : vehiculos) {
            if (v.getPlaca().equals(placa)) {
                v.setDisponible(true);
                System.out.println("✓ Vehículo devuelto: " + placa);
                return;
            }
        }
        System.out.println("✗ Vehículo no encontrado");
    }
    
    public static void main(String[] args) {
        SistemaAlquilerVehiculos sistema = new SistemaAlquilerVehiculos();
        
        // Agregar vehículos
        sistema.agregarVehiculo(new Auto("ABC-123", "Toyota", "Corolla", 40));
        sistema.agregarVehiculo(new Auto("DEF-456", "Honda", "Civic", 45));
        sistema.agregarVehiculo(new SUV("GHI-789", "Ford", "Explorer", 60));
        sistema.agregarVehiculo(new SUV("JKL-012", "Toyota", "Highlander", 65));
        sistema.agregarVehiculo(new Camion("MNO-345", "Volvo", "FH16", 100));
        sistema.agregarVehiculo(new Deportivo("PQR-678", "Ferrari", "F8", 200));
        sistema.agregarVehiculo(new Deportivo("STU-901", "Porsche", "911", 180));
        
        // Mostrar información
        sistema.mostrarTodosVehiculos();
        sistema.mostrarVehiculosDisponibles();
        sistema.mostrarMarcas();
        
        // Simulación de alquiler
        sistema.alquilarVehiculo("ABC-123", 5);
        sistema.alquilarVehiculo("GHI-789", 3);
        sistema.alquilarVehiculo("PQR-678", 2);
        
        // Mostrar vehículos disponibles después de alquilar
        sistema.mostrarVehiculosDisponibles();
        
        // Devoluciones
        sistema.devolverVehiculo("ABC-123");
        
        // Mostrar estado final
        sistema.mostrarVehiculosDisponibles();
    }
}
```

### Salida Esperada

```
=== TODOS LOS VEHÍCULOS ===
Placa: ABC-123 | Marca: Toyota | Modelo: Corolla | Tarifa: $40.0/día | Disponible: SÍ
Placa: DEF-456 | Marca: Honda | Modelo: Civic | Tarifa: $45.0/día | Disponible: SÍ
Placa: GHI-789 | Marca: Ford | Modelo: Explorer | Tarifa: $60.0/día | Disponible: SÍ
Placa: JKL-012 | Marca: Toyota | Modelo: Highlander | Tarifa: $65.0/día | Disponible: SÍ
Placa: MNO-345 | Marca: Volvo | Modelo: FH16 | Tarifa: $100.0/día | Disponible: SÍ
Placa: PQR-678 | Marca: Ferrari | Modelo: F8 | Tarifa: $200.0/día | Disponible: SÍ
Placa: STU-901 | Marca: Porsche | Modelo: 911 | Tarifa: $180.0/día | Disponible: SÍ

=== VEHÍCULOS DISPONIBLES ===
Placa: ABC-123 | Marca: Toyota | Modelo: Corolla | Tarifa: $40.0/día | Disponible: SÍ
Placa: DEF-456 | Marca: Honda | Modelo: Civic | Tarifa: $45.0/día | Disponible: SÍ
Placa: GHI-789 | Marca: Ford | Modelo: Explorer | Tarifa: $60.0/día | Disponible: SÍ
Placa: JKL-012 | Marca: Toyota | Modelo: Highlander | Tarifa: $65.0/día | Disponible: SÍ
Placa: MNO-345 | Marca: Volvo | Modelo: FH16 | Tarifa: $100.0/día | Disponible: SÍ
Placa: PQR-678 | Marca: Ferrari | Modelo: F8 | Tarifa: $200.0/día | Disponible: SÍ
Placa: STU-901 | Marca: Porsche | Modelo: 911 | Tarifa: $180.0/día | Disponible: SÍ

=== MARCAS DE VEHÍCULOS ===
- Honda
- Ford
- Volvo
- Toyota
- Ferrari
- Porsche

✓ Vehículo alquilado exitosamente
Placa: ABC-123 | Días: 5 | Costo Total: $200.00

✓ Vehículo alquilado exitosamente
Placa: GHI-789 | Días: 3 | Costo Total: $230.00

✓ Vehículo alquilado exitosamente
Placa: PQR-678 | Días: 2 | Costo Total: $500.00

=== VEHÍCULOS DISPONIBLES ===
Placa: DEF-456 | Marca: Honda | Modelo: Civic | Tarifa: $45.0/día | Disponible: SÍ
Placa: JKL-012 | Marca: Toyota | Modelo: Highlander | Tarifa: $65.0/día | Disponible: SÍ
Placa: MNO-345 | Marca: Volvo | Modelo: FH16 | Tarifa: $100.0/día | Disponible: SÍ
Placa: STU-901 | Marca: Porsche | Modelo: 911 | Tarifa: $180.0/día | Disponible: SÍ

✓ Vehículo devuelto: ABC-123

=== VEHÍCULOS DISPONIBLES ===
Placa: ABC-123 | Marca: Toyota | Modelo: Corolla | Tarifa: $40.0/día | Disponible: SÍ
Placa: DEF-456 | Marca: Honda | Modelo: Civic | Tarifa: $45.0/día | Disponible: SÍ
Placa: JKL-012 | Marca: Toyota | Modelo: Highlander | Tarifa: $65.0/día | Disponible: SÍ
Placa: MNO-345 | Marca: Volvo | Modelo: FH16 | Tarifa: $100.0/día | Disponible: SÍ
Placa: STU-901 | Marca: Porsche | Modelo: 911 | Tarifa: $180.0/día | Disponible: SÍ
```

---

## Conceptos Cubiertos en Ambos Ejercicios

| Concepto | Ejercicio 1 | Ejercicio 2 |
|----------|-----------|-----------|
| **Clase Abstracta** | ✓ Empleado | ✓ Vehiculo |
| **Herencia** | ✓ 3 niveles | ✓ 4 clases descendientes |
| **Polimorfismo** | ✓ calcularSalarioFinal() | ✓ calcularCostoAlquiler() |
| **ArrayList** | ✓ Almacena empleados | ✓ Almacena vehículos |
| **HashSet** | ✓ Departamentos únicos | ✓ Marcas únicas |
| **Métodos Override** | ✓ Implementación específica | ✓ Implementación específica |
| **Objetos** | ✓ Instancias de empleados | ✓ Instancias de vehículos |
