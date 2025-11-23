package und4;

import java.util.Scanner; 

public class Ejercicio6HOja4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	Scanner entrada = new Scanner (System.in);
	
	int [] numeros = new int [3];
	
	for(int i = 0 ; i < 3 ;  i++ ) {
		
		int num = entrada.nextInt();
		
		numeros[i] = num ;
		
	}
	
	
	int suma = 0 ;
	
	 
	
	for (int y = 0 ; y < 3 ; y++ ) {
		
		 suma += numeros[y];
		 
	}
	System.out.println("esto es la suma " +  suma);
	
	// multiplicacion
	
	
	int mult = 1 ; 
	
	for (int x = 0 ; x < 3 ; x++ ) {
		
		 mult *= numeros[x] ; 
		 
	}
	
	System.out.println("es=to es la mutliploicacion " + mult );
	 
	// division
	
	int divi = 0 ; 

	for (int z = 0 ; z < 3 - 1; z++ ) {
		

		
	}
	
   System.out.println("la division es  " + divi / 3  );
	

    
     
   
   
   
	
	}
	

}
