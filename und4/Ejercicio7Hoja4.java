package und4;

import java.util.Scanner ;

public class Ejercicio7Hoja4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner entrada = new Scanner(System.in);
		
		
		int [] numeros = new int [10];
		
		int num ;
		for(int i = 0 ; i < 10 ; i++ ) {
			
			
			
			System.out.println("ingrese el numero " + i );
			num =entrada.nextInt();
	
			numeros[i] += num ; 
			
			
		}
		
		
		
       
		// para ordenador de forma ascendete es decir de menor a mayor 
		
		
	 
		for(int i = 0 ; i < numeros.length - 1   ; i++ ) {
			
			for (int j = 0 ; j < numeros.length - 1 ; j++ ) {
				
				 
				 if(numeros[j] > numeros[j+ 1]) {
					 
					 int temp = numeros[j];
					 numeros[j] = numeros[j + 1];
					 numeros[j+1] = temp ; 
				 }
				
			}
		}
		
		
		for(int y : numeros )System.out.print(y + " ");
		
		
		
	}

}
