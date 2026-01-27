package javaintroducion;

public class PruebaCuenta {

	public static void main(String[] args) {
		Cuenta cuan_per1 = new Cuenta("402042",0);
		Cuenta cuan_per1_sin_fondo = new Cuenta("402042", 700);
		Persona per = new Persona("402042", null);
		// ingresar dinero en la primera cuenta
		cuan_per1.recibirABonons(1100);
		//pagar alquiler 

		cuan_per1_sin_fondo.PagarRecibo(cuan_per1_sin_fondo.consultar_saldo() - 750);
		// comrobar si la persona es morosa 
		if(per.esMorosa(cuan_per1_sin_fondo.consultar_saldo())){
			System.out.println(" No Es morosa");
		}else{
			System.out.println("Es morosa");
		}
		// trasnferencia de una cuenta a otra y comprobar mostrnadolo por pantall que cambia el estado de la persona 
		// pagamos 
		
		


	}

}
