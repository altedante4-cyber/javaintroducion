package und4;

import java.util.Scanner;

public class Ejercicio12Dis {
	static final int TAM=5;
	 // esto es na constante global 
	 
	static Scanner entrada = new Scanner (System.in );
	public static void main(String[] args) {
		// TODO Auto-generated method stub
   int [] numeros = new int[TAM];
   
		
	//	numeros = rellenar(numeros); esto es del primer public 
   
       rellenar(numeros);
		
		for (int i = 0 ; i < TAM ; i++ ) {
			System.out.println(numeros[i]);
			
		}
		
	}
	
  // esto es un primera opcion 
	//public static int[] rellenar(int [] nums) {
		
		//for (int i = 0 ; i < TAM ; i++ ) {
			
			//System.out.println("introduce numero");
			
		//	nums[i] = entrada.nextInt();
		//	
		//}
	
	public static void rellenar(int [] nums ) {
		
		for (int i=0 ; i< TAM ; i++ ) {
			
			System.out.println("introduce numero");
			nums[i] = entrada.nextInt();
		}
		
		// paso por vlaor(copia)
		//cualquier variable
		// paos por referencai (DIR  de mem)
		// ARRAY,OBJETO 
	}

}
