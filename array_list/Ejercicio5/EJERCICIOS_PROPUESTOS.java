/*
 * EJERCICIOS PROPUESTOS PARA PRACTICAR
 * 
 * Basándose en el sistema de vehículos, realiza los siguientes ejercicios:
 */

// EJERCICIO 1: Agregar una nueva clase de vehículo
// ================================================
/*
 * Crea una clase "Bicicleta" que herede de Vehiculo con:
 * - Atributos: tipo (BMX, Montaña, Ruta), cambios
 * - Implementa mostrarInfo() con formato específico para bicicleta
 * - Implementa calcularImpuesto() (sugerencia: 2% del precio)
 * - Agrégax método pedalear()
 * 
 * Pista de implementación:
 * public class Bicicleta extends Vehiculo {
 *     private String tipo;
 *     private int cambios;
 *     ...
 * }
 */


// EJERCICIO 2: Método de búsqueda avanzada
// =========================================
/*
 * En la clase GestorVehiculos, crea un método:
 * public ArrayList<Vehiculo> buscarPorRangoPrecios(double minimo, double maximo)
 * 
 * Que retorne todos los vehículos cuyo precio esté entre el mínimo y máximo.
 * 
 * Ejemplo de uso:
 * ArrayList<Vehiculo> baratos = gestor.buscarPorRangoPrecios(0, 25000);
 */


// EJERCICIO 3: Ordenamiento
// ==========================
/*
 * Crea un método en GestorVehiculos que ordene los vehículos por precio:
 * public void ordenarPorPrecio()
 * 
 * Puedes usar Collections.sort() con un Comparator o hacer un ordenamiento manual.
 * 
 * Pista:
 * import java.util.Collections;
 * Collections.sort(vehiculos, new Comparator<Vehiculo>() {
 *     @Override
 *     public int compare(Vehiculo v1, Vehiculo v2) {
 *         return Double.compare(v1.getPrecio(), v2.getPrecio());
 *     }
 * });
 */


// EJERCICIO 4: Filtrado de vehículos
// ==================================
/*
 * Crea un método que retorne solo los vehículos posteriores a un año específico:
 * public ArrayList<Vehiculo> vehiculosDesdeAño(int año)
 * 
 * Ejemplo:
 * ArrayList<Vehiculo> nuevos = gestor.vehiculosDesdeAño(2023);
 */


// EJERCICIO 5: Estadísticas
// =========================
/*
 * Crea un método que calcule el precio promedio de los vehículos:
 * public double calcularPrecioPromedio()
 * 
 * Y otro que retorne el vehículo más barato:
 * public Vehiculo obtenerVehiculoMasBarato()
 */


// EJERCICIO 6: Método toString()
// ==============================
/*
 * Agregx el método toString() a la clase Vehiculo y a sus subclases.
 * Esto te permitirá hacer:
 * System.out.println(vehiculo); // En lugar de vehiculo.mostrarInfo()
 * 
 * Ejemplo:
 * @Override
 * public String toString() {
 *     return "Coche{" +
 *         "marca='" + marca + '\'' +
 *         ", modelo='" + modelo + '\'' +
 *         ", precio=" + precio +
 *         '}';
 * }
 */


// EJERCICIO 7: Método equals() y hashCode()
// ==========================================
/*
 * Dos vehículos son iguales si tienen la misma marca y modelo.
 * Implementa equals() y hashCode() en la clase Vehiculo.
 * 
 * Esto te permitirá usar:
 * vehiculos.contains(vehiculo);
 * vehiculos.indexOf(vehiculo);
 */


// EJERCICIO 8: Interactividad
// ===========================
/*
 * Crea un programa interactivo en consola que permita:
 * 1. Agregar un nuevo vehículo
 * 2. Mostrar todos los vehículos
 * 3. Buscar un vehículo por marca
 * 4. Calcular impuestos
 * 5. Eliminar un vehículo
 * 6. Salir
 * 
 * Usa un menú con opciones numéricas y Scanner para leer entrada del usuario.
 */


// EJERCICIO 9: Persistencia de datos
// ==================================
/*
 * Guarda los vehículos a un archivo de texto y carga desde el archivo.
 * 
 * Métodos a crear:
 * public void guardarEnArchivo(String nombreArchivo)
 * public void cargarDesdeArchivo(String nombreArchivo)
 * 
 * Usa FileWriter/FileReader o PrintWriter/BufferedReader
 */


// EJERCICIO 10: Clase abstracta (DESAFÍO AVANZADO)
// ================================================
/*
 * Este es un desafío para después.
 * Convierte Vehiculo en una clase abstracta y:
 * - Haz que mostrarInfo() sea abstracto (cada subclase DEBE implementarlo)
 * - Agregx un método abstracto acelerar() que cada vehículo implemente diferente
 * 
 * Mantén Vehiculo como clase regular POR AHORA para este ejercicio.
 */


// SOLUCIONES Y AYUDA
// ==================
/*
 * Las soluciones a estos ejercicios están disponibles en el archivo:
 * EjerciciosSoluciones.java
 * 
 * No mires la solución demasiado rápido. Intenta resolver cada ejercicio
 * antes de verificar la solución.
 */
