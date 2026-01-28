package javaintroducion;

public class Cuenta {
		
		private double  saldo ;
		private String n_cuenta ; 
		
		// inicialisamo el objeto  
		
		 public  Cuenta(String n_cuenta) {
			  
			 this.n_cuenta = n_cuenta ;
			 // ojo con esto  siempre hay que incialisar los atributos
			 saldo = 0.0 ;  
		 }
		 
		 
		 // creacion de los getter 
		 
		 public double consultar_saldo() {
			   
			 return saldo ; 
			   
			  
		 }
		 
		 public String dameCuenta() {
			   
			 return n_cuenta ; 
			 
		 }
		 
		 
		 // creacion de los setter 
		 public  boolean recibirABonons(double cant) {
			 if(cant >=0 ) {
				 saldo += cant ; 
				 return true ; 
			 }
			 
			return false ; 
		 }
		 
		 
		 public boolean PagarRecibo(double cant ) {
			 if(cant < 0 ) {
				  saldo -= cant ;
				  return true ;
			 }
			 
			 return false ; 
			  
		 }

		 //getter
		 
		 public String toString() {
			  return "Numero Cuent:"+n_cuenta+"Saldo:"+saldo ; 
			  
		 }
		 
		 
		 
		
		
}
