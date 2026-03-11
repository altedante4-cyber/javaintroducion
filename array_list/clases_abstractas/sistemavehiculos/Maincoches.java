package sistemavehiculos;

public class Maincoches {
    public static void main(String[] args) {
        Vehiculo[] misAutos = new Vehiculo[3];

        misAutos[0] = new Coche("Ford", "Raptor", 200, 6);
        misAutos[1] = new Moto("Suzuki", "Najatu", 250, 100);
        misAutos[2] = new Coche("Mercedes", "C1", 300, 4);

        for (Vehiculo v : misAutos) {
            v.mostrarInfo();
        }

        System.out.println("\n--- Después de acelerar 50 km/h ---\n");
        
        for (Vehiculo v : misAutos) {
            v.acelerar(50);
            v.mostrarInfo();
        }
    }
}
