package und4;

import java.util.Scanner ; 
public class EJE4Hoj4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		// que rellene un rray con 20 numeros y luego busque un numero entero encontado
		
		
		Scanner entrada = new Scanner (System.in );
		
		 int [] numeros = new int [20];

		 int num , num2 ; 
		
		for (int i = 0 ; i < 20 ; i++ ) {
			
			System.out.println("Ingrese el numero ");
			
			num2 = entrada.nextInt();
			
			numeros[i] += num2 ; 
			
		}
		
		
		// buscar numero 
		
		
		System.out.println("ingreese el numero que dese buscar ");
		
		
		num = entrada.nextInt();
		
	
		
		for ( int j = 0 ; j < numeros.length   ; j++ ) {
			
			
			 if ( num == numeros[j] ) {
				 
				System.out.println("encontrado en posicion" + j);
			 }else {
				 
				 System.out.println("posicion no encontrada");
				 break;
			 }
			 
			 
			
		}
		
	

		
		
	}

}
