package javaintroducion;

public class PruebaCuenta {

	public static void main(String[] args) {
		
		Persona p1=new Persona("1234a");
		Cuenta c1=new Cuenta("0");
		Cuenta c2 = new Cuenta("700");
		
		
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
		
		
		
		
		if(p1.agregarcuenta(c2)) {
			
			boolean retirar_dinero = c2.PagarRecibo(750);
			
			if(retirar_dinero) {
				
				System.out.println(p1.toString());
			}else {
				System.out.println("la persona es morosa ");
			}
			
			// comprobar si esta persona es morosa o no 
		
			
		}else {
			System.out.println("NO se agrego a la cuenta ");  
		}
		

		
		

	}

}
