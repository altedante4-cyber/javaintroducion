package und4;

import java.util.Scanner;

import java.util.Scanner  ;
public class Ejercio8Hoja4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner entrada = new Scanner (System.in);
		// que lea 10 numeros por teclado 5 para un array y 5 para otro array distinto . MOstrar los 10 numeros en pantlala mediante nun solo array 
		
		
		int [] num = new int [5];
		int [] num1 = new int [5];
		int [] numero = new int [10];
		
		
		for(int i = 0 ; i < 5 ; i++ ){
			
			System.out.println("ingrese los primeros 5 numeros " + i );
			
			int n =entrada.nextInt();
			
			num[i] += n ;
			
			
		}
		
	  
		
		System.out.println();
		
		System.out.println("ahora ingresa los otros 5 numeros ");
		
	
		 for (int j = 0 ; j < 10 ; j++ ) {
			 System.out.println("ingrese los segundos numeros " + j );
			 
			 int nn = entrada.nextInt();
			 
			 num1[j] += nn ; 
			 
			 for (int q = 0 ;  q < j ; q++ ) {
					
					numero[q] += num1[j]; 
					
				    
				}
		 }
		 
		
	
		
		

	}

}
