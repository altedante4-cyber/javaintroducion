package javaintroducion;

public class PruebaCuenta {

	public static void main(String[] args) {
		
		Persona p1=new Persona("1234a");
		Cuenta c1=new Cuenta("001",0);
		Cuenta c2 = new Cuenta("002",700);
		
		
		// agregamos cuenta a la persona1 
		
		if(p1.agregarcuenta(c1)) {

			
			boolean recibir_nomina =  c1.recibirABonons(1000);
			
			if(recibir_nomina) {
				 
				System.out.println(p1.toString());
			}else {
				System.out.println("La operacion no se realizao corectmanete ");
			}
			
			
			 
		}else {
			System.out.println("NO se agrego la cuenta ");
		}

		
if (c1.PagarRecibo(100)) {
    c2.recibirABonons(100);
    System.out.println("Transferencia exitosa.");
} else {
    System.out.println("Fallo: Saldo insuficiente en c2.");
}

System.out.println(c1.toString());
System.out.println(c2.toString());

// Creo una cuenta asociada a p1 
//Creando un objeto anonimo

// agregar una cuenta de forma anonima
// p1.agregarCUenta(new Cuenta("2"))




	}

}
