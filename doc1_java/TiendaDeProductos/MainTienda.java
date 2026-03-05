package TiendaDeProductos;

public class MainTienda {
    public static void main(String[] args) {
        Tienda miTienda = new Tienda();

        // Agregamos 4 productos
        miTienda.agregarProducto(new Producto("Azucar", 20.0, 10));
        miTienda.agregarProducto(new Producto("Arroz", 15.0, 5));
        miTienda.agregarProducto(new Producto("Leche", 45.0, 12));
        miTienda.agregarProducto(new Producto("Cafe", 80.0, 2));

        // Mostramos
        miTienda.mostrarCatalogo();

        // Calculamos valor
        double total = miTienda.calcularValorTotal();
        System.out.println("\nValor total del inventario: $" + total);

        // Buscamos
        String buscar = "Leche";
        Producto resultado = miTienda.buscarPorNombre(buscar);

        if (resultado != null) {
            System.out.println("Encontrado: " + resultado);
        } else {
            System.out.println("El producto " + buscar + " no existe.");
        }
    }
}