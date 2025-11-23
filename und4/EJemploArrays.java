package und4;

import java.util.Scanner ; 
public class EJemploArrays {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		Scanner entrada = new Scanner(System.in);
		
    
		
		   int [] notas ;
		   
		   notas = new int[8];
		   
		   int suma =  0 ;
		   
		   double media;
		   
		   int i = 0 ; 
		   for ( i = 0 ; i < 8 ; i++ ) {
			   
			   System.out.println("introduce nota " + (i +  1) +  ":");
			   notas[i] =entrada.nextInt();
			   suma = suma+notas[i];
		   }
		
		  System.out.print("la media e "  + (suma / 8.0));
		  
		  // mostrar las notas del alumno
		  
		  for (i = 0 ; i < 8 ; i++ ) {
			  
			  System.out.println("NOta:" + notas[i] );
			  
		  }
		
	}

}
