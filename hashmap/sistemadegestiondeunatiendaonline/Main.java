package sistemadegestiondeunatiendaonline;

public class Main {
    public static void main(String[] args) {
        TiendaOnline miTienda = new TiendaOnline();

        // 1. Agregar 6 productos (2 de cada tipo para variedad)
        miTienda.agregarProducto(new ProductoFisico(1, "Laptop", 800.0, "Electrónica", 2.5, 15.0));
        miTienda.agregarProducto(new ProductoFisico(2, "Camiseta", 20.0, "Ropa", 0.2, 5.0));
        miTienda.agregarProducto(new ProductoDigital(3, "E-book Java", 15.0, "Libros", 500));
        miTienda.agregarProducto(new ProductoDigital(4, "Antivirus", 30.0, "Software", 200));
        miTienda.agregarProducto(new ProductoServicio(5, "Consultoría SEO", 100.0, "Consultoría", 30 ));
        miTienda.agregarProducto(new ProductoServicio(6, "Diseño Web", 200.0, "Consultoría", 2));

        // 2. Registrar 3 clientes (incluyendo un duplicado por email)
        Cliente c1 = new Cliente(101, "Ana Garcia", "ana@email.com");
        Cliente c2 = new Cliente(102, "Luis Perez", "luis@email.com");
        Cliente c3 = new Cliente(103, "Ana Garcia", "ana@email.com"); // Duplicado intencional

        miTienda.registrarClientes(c1);
        miTienda.registrarClientes(c2);
        miTienda.registrarClientes(c3); // Debería ser ignorado por el HashSet

        // 3. Mostrar categorías, productos y filtrar
        System.out.println("--- Categorías Disponibles ---");
        miTienda.mostrarCategorias();

        System.out.println("\n--- Lista de todos los productos ---");
        miTienda.listarProductos();

        System.out.println("\n--- Filtrado por categoría: Consultoría ---");
        miTienda.listarProductosPorCategoria("Consultoría");

        // 4. Agregar items al carrito
        miTienda.agregarAlCarrito(1, 1); // Laptop
        miTienda.agregarAlCarrito(3, 2); // 2 E-books
        miTienda.agregarAlCarrito(5, 1); // Consultoría

        // 5. Mostrar carrito y totales
        System.out.println("\n--- Contenido del Carrito ---");
        miTienda.listarCarrito();
        
        System.out.println("\nTotal sin descuento: $" + miTienda.calcularTotal());
        
        double total =  miTienda.aplicarDescuento(10.0); // Aplicamos un 10% adicional
        System.out.println("Total con descuento final aplicado: $" +total  );
        
        System.out.println("\n--- Lista de Clientes Registrados ---");
        miTienda.listarClientes();
    }
}
