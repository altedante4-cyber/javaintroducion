public class ProductoServicio extends Producto {
    private int duracionDias;

    public ProductoServicio(int id, String nombre, double precio, String categoria, 
                            int duracionDias) {
        super(id, nombre, precio, categoria);
        this.duracionDias = duracionDias;
    }

    public int getDuracionDias() {
        return duracionDias;
    }

    @Override
    public double calcularPrecioFinal() {
        double iva = getPrecio() * 0.21;
        double precioConIva = getPrecio() + iva;
        double descuento = precioConIva * 0.05;
        return precioConIva - descuento;
    }

    @Override
    public String obtenerDescripcion() {
        return "Servicio: " + getNombre() + " - Duración: " + duracionDias + " días";
    }

    @Override
    public String toString() {
        return "ProductoServicio{id=" + getId() + ", nombre='" + getNombre() + 
               "', precio=" + getPrecio() + ", categoria='" + getCategoria() + 
               "', duracionDias=" + duracionDias + ", precioFinal=" + calcularPrecioFinal() + "}";
    }
}
