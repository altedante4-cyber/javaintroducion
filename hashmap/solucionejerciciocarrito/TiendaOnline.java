import java.util.HashMap;
import java.util.HashSet;
import java.util.ArrayList;

public class TiendaOnline {
    private HashMap<Integer, Producto> productos;
    private HashSet<Cliente> clientes;
    private ArrayList<ItemCarrito> carrito;
    private String[] categorias;

    public TiendaOnline() {
        this.productos = new HashMap<>();
        this.clientes = new HashSet<>();
        this.carrito = new ArrayList<>();
        this.categorias = new String[]{"Electrónica", "Ropa", "Software", "Consultoría", "Libros"};
    }

    public void agregarProducto(Producto producto) {
        productos.put(producto.getId(), producto);
    }

    public Producto obtenerProducto(int id) {
        return productos.get(id);
    }

    public void listarProductos() {
        System.out.println("\n=== LISTA DE PRODUCTOS ===");
        for (Producto p : productos.values()) {
            System.out.println(p);
        }
    }

    public void listarProductosPorCategoria(String categoria) {
        System.out.println("\n=== PRODUCTOS EN CATEGORÍA: " + categoria + " ===");
        for (Producto p : productos.values()) {
            if (p.getCategoria().equalsIgnoreCase(categoria)) {
                System.out.println(p);
            }
        }
    }

    public void registrarCliente(Cliente cliente) {
        if (clientes.add(cliente)) {
            System.out.println("Cliente registrado: " + cliente.getNombre());
        } else {
            System.out.println("El cliente con email " + cliente.getEmail() + " ya existe (duplicado)");
        }
    }

    public void listarClientes() {
        System.out.println("\n=== LISTA DE CLIENTES ===");
        for (Cliente c : clientes) {
            System.out.println(c);
        }
    }

    public void agregarAlCarrito(int idProducto, int cantidad) {
        Producto producto = productos.get(idProducto);
        if (producto != null) {
            ItemCarrito item = new ItemCarrito(producto, cantidad);
            carrito.add(item);
            System.out.println("Agregado al carrito: " + producto.getNombre() + " x" + cantidad);
        } else {
            System.out.println("Producto con ID " + idProducto + " no encontrado");
        }
    }

    public void listarCarrito() {
        System.out.println("\n=== CARRITO DE COMPRAS ===");
        for (ItemCarrito item : carrito) {
            System.out.println(item);
        }
    }

    public void vaciarCarrito() {
        carrito.clear();
        System.out.println("Carrito vaciado");
    }

    public double calcularTotal() {
        double total = 0;
        for (ItemCarrito item : carrito) {
            total += item.calcularSubtotal();
        }
        return total;
    }

    public double aplicarDescuento(double porcentaje) {
        double total = calcularTotal();
        double descuento = total * (porcentaje / 100);
        return total - descuento;
    }

    public void mostrarCategorias() {
        System.out.println("\n=== CATEGORÍAS DISPONIBLES ===");
        for (String cat : categorias) {
            System.out.println("- " + cat);
        }
    }
}
