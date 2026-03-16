public class ProductoDigital extends Producto {
    private double tamanoMB;

    public ProductoDigital(int id, String nombre, double precio, String categoria, 
                           double tamanoMB) {
        super(id, nombre, precio, categoria);
        this.tamanoMB = tamanoMB;
    }

    public double getTamanoMB() {
        return tamanoMB;
    }

    @Override
    public double calcularPrecioFinal() {
        double iva = getPrecio() * 0.21;
        return getPrecio() + iva;
    }

    @Override
    public String obtenerDescripcion() {
        return "Producto Digital: " + getNombre() + " - Tamaño: " + tamanoMB + "MB";
    }

    @Override
    public String toString() {
        return "ProductoDigital{id=" + getId() + ", nombre='" + getNombre() + 
               "', precio=" + getPrecio() + ", categoria='" + getCategoria() + 
               "', tamanoMB=" + tamanoMB + ", precioFinal=" + calcularPrecioFinal() + "}";
    }
}
