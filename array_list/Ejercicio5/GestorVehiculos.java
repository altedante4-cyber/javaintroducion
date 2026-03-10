import java.util.ArrayList;

public class GestorVehiculos {
    private ArrayList<Vehiculo> vehiculos;
    
    public GestorVehiculos() {
        vehiculos = new ArrayList<>();
    }
    
    // Agregar un vehículo de cualquier tipo (Polimorfismo)
    public void agregarVehiculo(Vehiculo v) {
        vehiculos.add(v);
        System.out.println("Vehículo agregado exitosamente");
    }
    
    // Mostrar todos los vehículos (Polimorfismo en acción)
    public void mostrarTodosLosVehiculos() {
        System.out.println("\n========== LISTA DE VEHÍCULOS ==========");
        if (vehiculos.isEmpty()) {
            System.out.println("No hay vehículos registrados");
            return;
        }
        
        for (int i = 0; i < vehiculos.size(); i++) {
            System.out.println("\n[Vehículo " + (i + 1) + "]");
            vehiculos.get(i).mostrarInfo(); // Polimorfismo
        }
        System.out.println("\n========================================\n");
    }
    
    // Calcular impuesto total (Polimorfismo)
    public void mostrarImpuestos() {
        System.out.println("\n========== IMPUESTOS A PAGAR ==========");
        double impuestoTotal = 0;
        
        for (Vehiculo v : vehiculos) {
            double impuesto = v.calcularImpuesto();
            System.out.println(v.getMarca() + " " + v.getModelo() + ": $" + impuesto);
            impuestoTotal += impuesto;
        }
        
        System.out.println("----------------------------------------");
        System.out.println("Impuesto total: $" + impuestoTotal);
        System.out.println("=======================================\n");
    }
    
    // Buscar vehículos por marca
    public ArrayList<Vehiculo> buscarPorMarca(String marca) {
        ArrayList<Vehiculo> resultados = new ArrayList<>();
        
        for (Vehiculo v : vehiculos) {
            if (v.getMarca().equalsIgnoreCase(marca)) {
                resultados.add(v);
            }
        }
        
        return resultados;
    }
    
    // Contar vehículos por tipo
    public void contarVehiculosPorTipo() {
        int coches = 0;
        int motos = 0;
        int camiones = 0;
        
        for (Vehiculo v : vehiculos) {
            if (v instanceof Coche) {
                coches++;
            } else if (v instanceof Moto) {
                motos++;
            } else if (v instanceof Camion) {
                camiones++;
            }
        }
        
        System.out.println("\n========== CONTEO POR TIPO ==========");
        System.out.println("Coches: " + coches);
        System.out.println("Motos: " + motos);
        System.out.println("Camiones: " + camiones);
        System.out.println("Total: " + vehiculos.size());
        System.out.println("=====================================\n");
    }
    
    // Vehículo más caro
    public void mostrarVehiculoMasCaro() {
        if (vehiculos.isEmpty()) {
            System.out.println("No hay vehículos registrados");
            return;
        }
        
        Vehiculo masCaro = vehiculos.get(0);
        
        for (Vehiculo v : vehiculos) {
            if (v.getPrecio() > masCaro.getPrecio()) {
                masCaro = v;
            }
        }
        
        System.out.println("\n========== VEHÍCULO MÁS CARO ==========");
        masCaro.mostrarInfo();
        System.out.println("========================================\n");
    }
    
    // Eliminar vehículo por índice
    public void eliminarVehiculo(int indice) {
        if (indice >= 0 && indice < vehiculos.size()) {
            vehiculos.remove(indice);
            System.out.println("Vehículo eliminado exitosamente\n");
        } else {
            System.out.println("Índice inválido\n");
        }
    }
    
    // Obtener cantidad de vehículos
    public int obtenerCantidad() {
        return vehiculos.size();
    }
}
