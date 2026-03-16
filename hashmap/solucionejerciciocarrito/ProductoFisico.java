public class ProductoFisico extends Producto {
    private double peso;
    private double costoEnvio;

    public ProductoFisico(int id, String nombre, double precio, String categoria, 
                          double peso, double costoEnvio) {
        super(id, nombre, precio, categoria);
        this.peso = peso;
        this.costoEnvio = costoEnvio;
    }

    public double getPeso() {
        return peso;
    }

    public double getCostoEnvio() {
        return costoEnvio;
    }

    @Override
    public double calcularPrecioFinal() {
        double iva = getPrecio() * 0.21;
        return getPrecio() + iva + costoEnvio;
    }

    @Override
    public String obtenerDescripcion() {
        return "Producto Físico: " + getNombre() + " - Peso: " + peso + "kg - Envío: $" + costoEnvio;
    }

    @Override
    public String toString() {
        return "ProductoFisico{id=" + getId() + ", nombre='" + getNombre() + 
               "', precio=" + getPrecio() + ", categoria='" + getCategoria() + 
               "', peso=" + peso + "kg, costoEnvio=" + costoEnvio + 
               ", precioFinal=" + calcularPrecioFinal() + "}";
    }
}
