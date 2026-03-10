public class Camion extends Vehiculo {
    private double capacidadCarga;
    private int numEjes;
    
    public Camion(String marca, String modelo, int año, double precio, 
                  double capacidadCarga, int numEjes) {
        super(marca, modelo, año, precio);
        this.capacidadCarga = capacidadCarga;
        this.numEjes = numEjes;
    }
    
    // Sobrescritura del método mostrarInfo (Polimorfismo)
    @Override
    public void mostrarInfo() {
        System.out.println("=== CAMIÓN ===");
        System.out.println("Marca: " + marca + ", Modelo: " + modelo);
        System.out.println("Año: " + año + ", Precio: $" + precio);
        System.out.println("Capacidad de carga: " + capacidadCarga + " toneladas, Ejes: " + numEjes);
    }
    
    // Sobrescritura del método calcularImpuesto (Polimorfismo)
    @Override
    public double calcularImpuesto() {
        return precio * 0.15; // 15% de impuesto para camiones
    }
    
    public void descargarCarga() {
        System.out.println("Descargando " + capacidadCarga + " toneladas del camión " + marca);
    }
    
    public double getCapacidadCarga() {
        return capacidadCarga;
    }
    
    public int getNumEjes() {
        return numEjes;
    }
}
