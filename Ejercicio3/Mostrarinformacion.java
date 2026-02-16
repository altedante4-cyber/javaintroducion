package Ejercicio3;

public class Mostrarinformacion {
	public static void main(String[] args) {
		Personal mio = new Personal("michael", "32904324","s" , "asa" , 2005 , 10 , 10 );
		profesores mio2 = new profesores("michael", "32904324","s" , "asa" , 20);
		
		System.out.println(mio.toString());
		System.out.println(mio2.toString());
	}
}
