public class Moto extends Vehiculo {
    private int cilindrada;
    private boolean tieneRefugio;
    
    public Moto(String marca, String modelo, int año, double precio, 
                int cilindrada, boolean tieneRefugio) {
        super(marca, modelo, año, precio);
        this.cilindrada = cilindrada;
        this.tieneRefugio = tieneRefugio;
    }
    
    // Sobrescritura del método mostrarInfo (Polimorfismo)
    @Override
    public void mostrarInfo() {
        System.out.println("=== MOTO ===");
        System.out.println("Marca: " + marca + ", Modelo: " + modelo);
        System.out.println("Año: " + año + ", Precio: $" + precio);
        System.out.println("Cilindrada: " + cilindrada + "cc, Refugio: " + (tieneRefugio ? "Sí" : "No"));
    }
    
    // Sobrescritura del método calcularImpuesto (Polimorfismo)
    @Override
    public double calcularImpuesto() {
        return precio * 0.08; // 8% de impuesto para motos
    }
    
    public void hacer_caballito() {
        System.out.println("¡La moto " + marca + " está haciendo un caballito!");
    }
    
    public int getCilindrada() {
        return cilindrada;
    }
    
    public boolean isTieneRefugio() {
        return tieneRefugio;
    }
}
