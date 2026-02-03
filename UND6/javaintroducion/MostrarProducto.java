package javaintroducion;
import java.util.Scanner;

public class MostrarProducto {

    public static void main(String[] args) {
        Tienda mitiTienda = new Tienda();
        Scanner sc = new Scanner(System.in);
        int option;

        do {
            System.out.println("\n--- MENÚ TIENDA ---");
            System.out.println("1. Dar de alta producto");
            System.out.println("2. Buscar producto");
            System.out.println("3. Modificar stock/precio");
            System.out.println("4. Salir");
            System.out.print("Seleccione una opción: ");
            
            option = sc.nextInt();
            sc.nextLine(); // Limpiar el buffer del Scanner

            switch (option) {
                case 1:
                    System.out.print("Nombre: ");
                    String name = sc.nextLine();
                    System.out.print("Precio: ");
                    double price = sc.nextDouble();
                    System.out.print("Stock: ");
                    int stock = sc.nextInt();

                    Producto nuevo = new Producto(name, price, stock);
                    if (mitiTienda.darAlta(nuevo)) {
                        System.out.println("¡Producto guardado!");
                    } else {
                        System.out.println("Error: Inventario lleno.");
                    }
                    break;

                case 2:
                    System.out.print("Nombre a buscar: ");
                    String buscar = sc.nextLine();
                    Producto encontrado = mitiTienda.getbuscarproducto(buscar);
                    if (encontrado != null) {
                        System.out.println("Resultado: " + encontrado.toString());
                    } else{
                        System.out.println("Producto no encontrado.");
                    }
                    break;

                case 3:
                    System.out.print("Nombre del producto a modificar: ");
                    String modNombre = sc.nextLine();
                    System.out.print("Nuevo precio: ");
                    double modPrecio = sc.nextDouble();
                    System.out.print("Nuevo stock: ");
                    int modStock = sc.nextInt();

                    if (mitiTienda.setmodificarstock(modNombre, modPrecio, modStock)) {
                        System.out.println("Datos actualizados correctamente.");
                    } else {
                        System.out.println("No se pudo encontrar el producto.");
                    }
                    break;

                case 4:
                    System.out.println("Ingrese el nombre del producto a borrar ");
                    String nama = sc.nextLine();

                    if(mitiTienda.getborrarproducto(nama)){
                        System.out.println("Borrado correctamete");
                    }else{
                        System.out.println("No se a podido borrar");
                    }


                case 5:
                    System.out.println("Cerrando programa...");
                    break;

                default:
                    System.out.println("Opción no válida.");
                    break;
            }
        } while (option != 5);
        
        sc.close();
    }
}