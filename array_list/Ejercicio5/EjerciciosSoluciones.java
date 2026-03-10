import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

/*
 * SOLUCIONES A EJERCICIOS PROPUESTOS
 * 
 * Este archivo contiene soluciones sugeridas para los ejercicios.
 * Úsalo como referencia después de intentar resolver por tu cuenta.
 */

// ============================================================
// EJERCICIO 1: Clase Bicicleta (Solución sugerida)
// ============================================================
class Bicicleta extends Vehiculo {
    private String tipo; // BMX, Montaña, Ruta
    private int cambios;
    
    public Bicicleta(String marca, String modelo, int año, double precio, 
                     String tipo, int cambios) {
        super(marca, modelo, año, precio);
        this.tipo = tipo;
        this.cambios = cambios;
    }
    
    @Override
    public void mostrarInfo() {
        System.out.println("=== BICICLETA ===");
        System.out.println("Marca: " + marca + ", Modelo: " + modelo);
        System.out.println("Año: " + año + ", Precio: $" + precio);
        System.out.println("Tipo: " + tipo + ", Cambios: " + cambios);
    }
    
    @Override
    public double calcularImpuesto() {
        return precio * 0.02; // 2% para bicicletas
    }
    
    public void pedalear() {
        System.out.println("Pedaleando en la " + tipo + " " + marca + " " + modelo);
    }
}


// ============================================================
// EJERCICIO 2: Búsqueda por rango de precios
// ============================================================
/*
 * En GestorVehiculos, agregx este método:
 */
class GestorVehiculos_Soluciones {
    private ArrayList<Vehiculo> vehiculos;
    
    public GestorVehiculos_Soluciones() {
        vehiculos = new ArrayList<>();
    }
    
    // SOLUCIÓN EJERCICIO 2
    public ArrayList<Vehiculo> buscarPorRangoPrecios(double minimo, double maximo) {
        ArrayList<Vehiculo> resultados = new ArrayList<>();
        
        for (Vehiculo v : vehiculos) {
            if (v.getPrecio() >= minimo && v.getPrecio() <= maximo) {
                resultados.add(v);
            }
        }
        
        return resultados;
    }
    
    
    // SOLUCIÓN EJERCICIO 3: Ordenar por precio
    public void ordenarPorPrecio() {
        Collections.sort(vehiculos, new Comparator<Vehiculo>() {
            @Override
            public int compare(Vehiculo v1, Vehiculo v2) {
                return Double.compare(v1.getPrecio(), v2.getPrecio());
            }
        });
        System.out.println("Vehículos ordenados por precio");
    }
    
    // Alternativa más moderna (Java 8+):
    public void ordenarPorPrecioModerno() {
        vehiculos.sort((v1, v2) -> Double.compare(v1.getPrecio(), v2.getPrecio()));
    }
    
    
    // SOLUCIÓN EJERCICIO 4: Filtrar por año
    public ArrayList<Vehiculo> vehiculosDesdeAño(int año) {
        ArrayList<Vehiculo> resultados = new ArrayList<>();
        
        for (Vehiculo v : vehiculos) {
            if (v.getAño() >= año) {
                resultados.add(v);
            }
        }
        
        return resultados;
    }
    
    
    // SOLUCIÓN EJERCICIO 5: Estadísticas
    public double calcularPrecioPromedio() {
        if (vehiculos.isEmpty()) {
            return 0;
        }
        
        double suma = 0;
        for (Vehiculo v : vehiculos) {
            suma += v.getPrecio();
        }
        
        return suma / vehiculos.size();
    }
    
    public Vehiculo obtenerVehiculoMasBarato() {
        if (vehiculos.isEmpty()) {
            return null;
        }
        
        Vehiculo masBarato = vehiculos.get(0);
        
        for (Vehiculo v : vehiculos) {
            if (v.getPrecio() < masBarato.getPrecio()) {
                masBarato = v;
            }
        }
        
        return masBarato;
    }
    
    
    // SOLUCIÓN EJERCICIO 6: toString() para Vehiculo
    /*
     * En la clase Vehiculo:
     * @Override
     * public String toString() {
     *     return this.getClass().getSimpleName() + "{" +
     *         "marca='" + marca + '\'' +
     *         ", modelo='" + modelo + '\'' +
     *         ", año=" + año +
     *         ", precio=$" + precio +
     *         '}';
     * }
     * 
     * Para Coche:
     * @Override
     * public String toString() {
     *     return "Coche{" +
     *         "marca='" + marca + '\'' +
     *         ", modelo='" + modelo + '\'' +
     *         ", puertas=" + numPuertas +
     *         ", combustible='" + tipoCombustible + '\'' +
     *         ", precio=$" + precio +
     *         '}';
     * }
     */
    
    
    // SOLUCIÓN EJERCICIO 7: equals() y hashCode()
    /*
     * En la clase Vehiculo:
     * @Override
     * public boolean equals(Object o) {
     *     if (this == o) return true;
     *     if (!(o instanceof Vehiculo)) return false;
     *     
     *     Vehiculo vehiculo = (Vehiculo) o;
     *     return marca.equals(vehiculo.marca) && 
     *            modelo.equals(vehiculo.modelo);
     * }
     * 
     * @Override
     * public int hashCode() {
     *     return marca.hashCode() + modelo.hashCode();
     * }
     */
    
    // Métodos básicos
    public void agregarVehiculo(Vehiculo v) {
        vehiculos.add(v);
    }
    
    public int obtenerCantidad() {
        return vehiculos.size();
    }
}


/*
 * SOLUCIÓN EJERCICIO 8: Menú interactivo
 * 
 * PSEUDOCÓDIGO:
 * 
 * public class MenuVehiculos {
 *     public static void main(String[] args) {
 *         GestorVehiculos gestor = new GestorVehiculos();
 *         Scanner scanner = new Scanner(System.in);
 *         boolean ejecutando = true;
 *         
 *         while (ejecutando) {
 *             System.out.println("\n=== MENÚ ===");
 *             System.out.println("1. Agregar vehículo");
 *             System.out.println("2. Mostrar todos");
 *             System.out.println("3. Buscar por marca");
 *             System.out.println("4. Mostrar impuestos");
 *             System.out.println("5. Eliminar vehículo");
 *             System.out.println("6. Salir");
 *             
 *             int opcion = scanner.nextInt();
 *             scanner.nextLine(); // Limpiar buffer
 *             
 *             switch (opcion) {
 *                 case 1:
 *                     // Pedir datos y agregar
 *                     System.out.print("Marca: ");
 *                     String marca = scanner.nextLine();
 *                     // ... más datos
 *                     break;
 *                 case 2:
 *                     gestor.mostrarTodosLosVehiculos();
 *                     break;
 *                 // ... más casos
 *                 case 6:
 *                     ejecutando = false;
 *                     break;
 *             }
 *         }
 *         
 *         scanner.close();
 *     }
 * }
 */


/*
 * SOLUCIÓN EJERCICIO 9: Persistencia
 * 
 * import java.io.*;
 * import java.util.Scanner;
 * 
 * public void guardarEnArchivo(String nombreArchivo) throws IOException {
 *     PrintWriter writer = new PrintWriter(new FileWriter(nombreArchivo));
 *     
 *     for (Vehiculo v : vehiculos) {
 *         writer.println(v.toString());
 *     }
 *     
 *     writer.close();
 * }
 * 
 * public void cargarDesdeArchivo(String nombreArchivo) throws IOException {
 *     Scanner scanner = new Scanner(new File(nombreArchivo));
 *     
 *     while (scanner.hasNextLine()) {
 *         String linea = scanner.nextLine();
 *         // Parsear la línea y crear un vehículo
 *         // ...
 *     }
 *     
 *     scanner.close();
 * }
 */


// ============================================================
// EJEMPLOS DE USO
// ============================================================
/*
 * Ejemplo de cómo usar las soluciones:
 * 
 * public class EjemploUso {
 *     public static void main(String[] args) {
 *         GestorVehiculos_Soluciones gestor = new GestorVehiculos_Soluciones();
 *         
 *         // Agregar vehículos
 *         gestor.agregarVehiculo(new Coche("Toyota", "Corolla", 2023, 25000, 4, "Gasolina"));
 *         gestor.agregarVehiculo(new Moto("Yamaha", "R6", 2023, 8000, 600, true));
 *         
 *         // Ejercicio 2: Buscar por rango
 *         ArrayList<Vehiculo> baratos = gestor.buscarPorRangoPrecios(0, 20000);
 *         System.out.println("Vehículos entre $0 y $20000: " + baratos.size());
 *         
 *         // Ejercicio 3: Ordenar
 *         gestor.ordenarPorPrecio();
 *         
 *         // Ejercicio 4: Filtrar por año
 *         ArrayList<Vehiculo> nuevos = gestor.vehiculosDesdeAño(2023);
 *         System.out.println("Vehículos desde 2023: " + nuevos.size());
 *         
 *         // Ejercicio 5: Estadísticas
 *         System.out.println("Precio promedio: $" + gestor.calcularPrecioPromedio());
 *         Vehiculo masBarato = gestor.obtenerVehiculoMasBarato();
 *         if (masBarato != null) masBarato.mostrarInfo();
 *     }
 * }
 */
