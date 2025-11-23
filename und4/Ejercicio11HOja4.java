package und4;


public class Ejercicio11HOja4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
		
		  

		
		int [] numeros = new int [102] ;
		for(int i = 0 ; i <= 100 ; i++ ) {
			
			if(i % 2 == 0 ) {
				
				numeros[i] = i ;
				
				System.out.println(i);
				
			}
		}
		
		
		int suma = 0 ; 
		
		for(int y = 0 ; y <= 100 ; y++ ) {
			
			if (numeros[y] != 0 ) {
				
				suma += numeros[y];
			
			
			}
		}
		
		
		System.out.println("esto es la suma "  + suma );
	
		
		
	}

}
