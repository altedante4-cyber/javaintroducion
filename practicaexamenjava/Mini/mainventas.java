package Mini;
import java.util.Scanner;

public class mainventas {
    static Scanner sc = new Scanner(System.in);
    static RegistroVentas ventas = new RegistroVentas();

    public static void main(String[] args) {
        int opcion; // Declaramos la variable fuera para que el while la reconozca

        do {
            mostrarmenu();
            System.out.print("Seleccione una opcion: ");
            opcion = sc.nextInt();
            sc.nextLine(); // Limpiar el buffer siempre después de un número

            switch (opcion) {
                case 1:
                    IngresarProducto();
                    break;
                case 2:
                    ventas.mostarProducto(); // Corregido el nombre del método
                    break;
                case 3:
                    EdicionProducto();
                    break;
                case 4:
                    // Aquí iría el método de eliminar o estadísticas
                    System.out.println("Funcionalidad en construcción...");
                    break;
                case 5:
                    System.out.println("Saliendo del sistema...");
                    break;
                default:
                    System.out.println("Opción no válida.");
                    break;
            }
        } while (opcion != 5); // Cambié a 5 para que coincida con la salida
    }

    public static void mostrarmenu() {
        System.out.println("\n--- SISTEMA MINI-MARKET ---");
        System.out.println("1. Registro de venta");
        System.out.println("2. Ver inventario de ventas");
        System.out.println("3. Editar precio de producto");
        System.out.println("4. Eliminar producto");
        System.out.println("5. Salir");
    }

    public static void IngresarProducto() {
        System.out.println("1. Ingresar todos los datos\n2. Solo nombre y precio (ID aleatorio)");
        int subOpcion = sc.nextInt();
        sc.nextLine(); // Limpiar buffer

        if (subOpcion == 1) {
            System.out.print("ID: ");
            int id = sc.nextInt();
            sc.nextLine(); // Limpiar buffer porque sigue un String
            System.out.print("Nombre: ");
            String nombre = sc.nextLine();
            System.out.print("Categoría: ");
            String categoria = sc.nextLine();
            System.out.print("Precio: ");
            double precio = sc.nextDouble();

            Producto nuevo = new Producto(id, nombre, categoria, precio);
            procesarResultado(ventas.agregarProducto(nuevo));

        } else if (subOpcion == 2) {
            System.out.print("Nombre: ");
            String nombre = sc.nextLine();
            System.out.print("Precio: ");
            double precio = sc.nextDouble();

            // Aquí se usa el constructor sobrecargado
            Producto nuevo2 = new Producto(nombre, precio);
            procesarResultado(ventas.agregarProducto(nuevo2));
        }
    }

    // Método auxiliar para no repetir código de confirmación
    private static void procesarResultado(boolean exito) {
        if (exito) {
            System.out.println("✅ Producto registrado con éxito.");
        } else {
            System.out.println("❌ Error: El registro está lleno.");
        }
    }

    public static void EdicionProducto() {
        System.out.print("Ingrese el ID del producto a editar: ");
        int id = sc.nextInt();

        // En RegistroVentas, buscarId debería devolver un boolean
        if (ventas.buscarId(id)) {
            System.out.print("Ingrese el nuevo precio: ");
            double precio = sc.nextDouble();
            ventas.editarPrecio(id, precio);
            System.out.println("✅ Precio actualizado.");
        } else {
            System.out.println("⚠️ No se encontró ningún producto con ese ID.");
        }
    }
}