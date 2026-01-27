package javaintroducion;

public class Cuenta {
		
		private double  saldo ;
		private String n_cuenta ; 
		
		// inicialisamo el objeto 
		
		 public  Cuenta(String n_cuenta , double saldo) {
			  
			 this.n_cuenta = n_cuenta ;
			 this.saldo = saldo ; 
			  
		 }
		 
		 
		 // creacion de los getter 
		 
		 public double consultar_saldo() {
			   
			 return saldo ; 
			   
			  
		 }
		 
		 
		 // creacion de los setter 
		 public  void recibirABonons(double saldo) {
			   
			   this.saldo = saldo ; 
			   
			   
		 }
		 
		 
		 public void PagarRecibo(double saldo ) {
			  
			 this.saldo = saldo ; 
		 }

		 // pagar cliente 
		 public double pagarcliente(double saldo_cliente1 , double saldo_cliente2){
					 return saldo_cliente1 += saldo_cliente2;

		 }
		
		
}
