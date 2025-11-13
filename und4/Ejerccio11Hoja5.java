package und4;

import java.util.Scanner; 
public class Ejerccio11Hoja5 {

	public static void main(String[] args) {
	
		Scanner entrada = new Scanner(System.in );

		System.out.println("ingrese el nunmero");
		int num = entrada.nextInt();
		
		int resultado = par(num);
		
		
		if (resultado == 0 ) {
			
			System.out.println("es par");
		}else {
			System.out.println("es impar");
		}

	}
	
	public static int par(int a )
	{
		
		int modulo = a % 2 ;
		  
			return modulo ; 
			
		
		
		
		
	  
	}

}
