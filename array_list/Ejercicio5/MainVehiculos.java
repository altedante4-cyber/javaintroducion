public class MainVehiculos {
    public static void main(String[] args) {
        GestorVehiculos gestor = new GestorVehiculos();
        
        System.out.println("===== SISTEMA DE GESTIÓN DE VEHÍCULOS =====\n");
        
        // Agregar coches
        System.out.println("--- Agregando Coches ---");
        gestor.agregarVehiculo(new Coche("Toyota", "Corolla", 2023, 25000, 4, "Gasolina"));
        gestor.agregarVehiculo(new Coche("BMW", "Serie 3", 2024, 50000, 4, "Diésel"));
        gestor.agregarVehiculo(new Coche("Honda", "Civic", 2022, 22000, 2, "Gasolina"));
        
        // Agregar motos
        System.out.println("\n--- Agregando Motos ---");
        gestor.agregarVehiculo(new Moto("Yamaha", "R6", 2023, 8000, 600, true));
        gestor.agregarVehiculo(new Moto("Harley-Davidson", "Sportster", 2022, 12000, 1200, false));
        
        // Agregar camiones
        System.out.println("\n--- Agregando Camiones ---");
        gestor.agregarVehiculo(new Camion("Volvo", "FH", 2023, 80000, 25, 3));
        gestor.agregarVehiculo(new Camion("Mercedes", "Actros", 2021, 75000, 20, 2));
        
        // Mostrar todos los vehículos
        gestor.mostrarTodosLosVehiculos();
        
        // Contar por tipo
        gestor.contarVehiculosPorTipo();
        
        // Mostrar impuestos
        gestor.mostrarImpuestos();
        
        // Vehículo más caro
        gestor.mostrarVehiculoMasCaro();
        
        // Buscar por marca
        System.out.println("========== BÚSQUEDA POR MARCA ==========");
        System.out.println("Buscando vehículos de 'Honda':");
        ArrayList<Vehiculo> resultados = gestor.buscarPorMarca("Honda");
        for (Vehiculo v : resultados) {
            v.mostrarInfo();
        }
        System.out.println("=======================================\n");
        
        // Demostración de métodos específicos (usando instanceof)
        System.out.println("========== MÉTODOS ESPECÍFICOS ==========");
        gestor.mostrarTodosLosVehiculos();
        
        // Ejecutar métodos específicos de cada tipo
        Vehiculo[] listaVehiculos = new Vehiculo[3];
        listaVehiculos[0] = new Coche("Fiat", "500", 2023, 20000, 2, "Gasolina");
        listaVehiculos[1] = new Moto("Ducati", "Monster", 2024, 15000, 937, true);
        listaVehiculos[2] = new Camion("Renault", "T", 2022, 70000, 18, 2);
        
        for (Vehiculo v : listaVehiculos) {
            v.mostrarInfo();
            
            // Polimorfismo con instanceof para acceder a métodos específicos
            if (v instanceof Coche) {
                ((Coche) v).abrirMaletero();
            } else if (v instanceof Moto) {
                ((Moto) v).hacer_caballito();
            } else if (v instanceof Camion) {
                ((Camion) v).descargarCarga();
            }
            System.out.println();
        }
        
        System.out.println("=======================================");
    }
}
