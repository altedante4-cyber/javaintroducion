package UND7;

public class UsoVehiculo {

	public static void main(String[] args) {
		
		Coche d1 = new Coche(true, 4, "Rojo", "1234-ABC", 150);
        
        System.out.println("Color del coche: " + d1.getColor());
        System.out.println("Potencia: " + d1.getCV() + " CV");
	}

}
