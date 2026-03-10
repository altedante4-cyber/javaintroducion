public class Coche extends Vehiculo {
    private int numPuertas;
    private String tipoCombustible;
    
    public Coche(String marca, String modelo, int año, double precio, 
                 int numPuertas, String tipoCombustible) {
        super(marca, modelo, año, precio);
        this.numPuertas = numPuertas;
        this.tipoCombustible = tipoCombustible;
    }
    
    // Sobrescritura del método mostrarInfo (Polimorfismo)
    @Override
    public void mostrarInfo() {
        System.out.println("=== COCHE ===");
        System.out.println("Marca: " + marca + ", Modelo: " + modelo);
        System.out.println("Año: " + año + ", Precio: $" + precio);
        System.out.println("Puertas: " + numPuertas + ", Combustible: " + tipoCombustible);
    }
    
    // Sobrescritura del método calcularImpuesto (Polimorfismo)
    @Override
    public double calcularImpuesto() {
        return precio * 0.12; // 12% de impuesto para coches
    }
    
    public void abrirMaletero() {
        System.out.println("Maletero del " + marca + " " + modelo + " abierto");
    }
    
    public int getNumPuertas() {
        return numPuertas;
    }
    
    public String getTipoCombustible() {
        return tipoCombustible;
    }
}
