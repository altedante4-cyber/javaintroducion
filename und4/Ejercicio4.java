package und4;


import java.util.Scanner ; 
public class Ejercicio4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
		Scanner entrada = new Scanner (System.in);
		
		System.out.println("Introduce letra 'p'=pares y 'i' = impares ");
		char letra = entrada.next().charAt(0);
		
		
		switch(letra) {
		
		case 'p' :
			
			for (int i = 1 ; i <= 500 ; i++ ) {
				
				if (i % 2 == 0) {
					
					System.out.println(i);
				}
			}
			break;
			
			
		case 'i' :
			
				for (int i = 1 ; i <= 500 ; i++ ) {
				
					if (i % 2 != 0) {
					
						System.out.println(i);
				}
			}
				break;
				
		
		default :
			
			System.out.println("Error letra invalida ");
				
				
		}
	}

}
