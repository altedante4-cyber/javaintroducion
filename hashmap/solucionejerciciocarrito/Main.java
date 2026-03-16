public class Main {
    public static void main(String[] args) {
        TiendaOnline tienda = new TiendaOnline();

        System.out.println("=== DEMOSTRACIÓN DEL SISTEMA DE GESTIÓN DE TIENDA ONLINE ===\n");

        // Agregar 6 productos de diferentes tipos
        System.out.println("--- AGREGANDO PRODUCTOS ---");
        
        ProductoFisico p1 = new ProductoFisico(1, "Laptop HP", 1000, "Electrónica", 2.5, 50);
        ProductoFisico p2 = new ProductoFisico(2, "Camiseta Nike", 30, "Ropa", 0.2, 5);
        ProductoDigital p3 = new ProductoDigital(3, "Adobe Photoshop", 300, "Software", 2000);
        ProductoDigital p4 = new ProductoDigital(4, "E-Book Java", 25, "Libros", 5);
        ProductoServicio p5 = new ProductoServicio(5, "Consultoría IT", 500, "Consultoría", 30);
        ProductoServicio p6 = new ProductoServicio(6, "Curso de Marketing", 200, "Consultoría", 15);

        tienda.agregarProducto(p1);
        tienda.agregarProducto(p2);
        tienda.agregarProducto(p3);
        tienda.agregarProducto(p4);
        tienda.agregarProducto(p5);
        tienda.agregarProducto(p6);
        
        // Registrar 3 clientes (incluyendo intento de duplicado)
        System.out.println("\n--- REGISTRANDO CLIENTES ---");
        Cliente c1 = new Cliente(1, "Juan Pérez", "juan@email.com");
        Cliente c2 = new Cliente(2, "María García", "maria@email.com");
        Cliente c3 = new Cliente(3, "Pedro López", "pedro@email.com");
        Cliente c3Duplicado = new Cliente(4, "Pedro Sánchez", "pedro@email.com"); // Mismo email

        tienda.registrarCliente(c1);
        tienda.registrarCliente(c2);
        tienda.registrarCliente(c3);
        tienda.registrarCliente(c3Duplicado); // Intento de duplicado

        // Mostrar categorías disponibles
        System.out.println();
        tienda.mostrarCategorias();

        // Listar todos los productos
        tienda.listarProductos();

        // Filtrar productos por categoría
        System.out.println();
        tienda.listarProductosPorCategoria("Electrónica");
        System.out.println();
        tienda.listarProductosPorCategoria("Consultoría");

        // Agregar items al carrito
        System.out.println("\n--- AGREGANDO AL CARRITO ---");
        tienda.agregarAlCarrito(1, 1); // Laptop HP x1
        tienda.agregarAlCarrito(3, 1);  // Adobe Photoshop x1
        tienda.agregarAlCarrito(5, 2);  // Consultoría IT x2
        tienda.agregarAlCarrito(2, 3);  // Camisetas x3

        // Mostrar carrito completo
        tienda.listarCarrito();

        // Mostrar total
        System.out.println("\n--- TOTALES ---");
        System.out.println("Total sin descuento: $" + tienda.calcularTotal());
        System.out.println("Total con 10% de descuento: $" + String.format("%.2f", tienda.aplicarDescuento(10)));

        // Vaciar carrito
        System.out.println();
        tienda.vaciarCarrito();

        // Listar clientes
        System.out.println();
        tienda.listarClientes();

        System.out.println("\n=== PROGRAMA FINALIZADO ===");
    }
}
