package und4;

import java.util.Scanner ; 
public class Ejercicio12HOja5 {
	 static final int TAM=5;
	 // esto es na constante global 
	 
	static Scanner entrada = new Scanner (System.in );
	 
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
    int [] numeros = new int[TAM];
 
	 numeros = rellenaArray();
	     
	     //mostramos el array
	     
	     for(int i =0 ; i < TAM ; i++) {
	    	 
	    	 System.out.print(numeros[i] + " ");
	    	 
	     }
		
		
	}
	
	public static int[] rellenaArray()
	{

	    
	     int[] nums = new int[TAM];
	     
	    // rellenamos el array 
	     for(int i = 0 ; i < TAM ; i++ ) {
	    	 
	    	 System.out.println("introduce numero ");
	    	 nums[i] = entrada.nextInt();
	     }
	     return nums ;  // devuelve a la linea donde fue llamada 
		
 		
	}

}
