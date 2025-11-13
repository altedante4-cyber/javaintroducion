package und4;

import java.util.Scanner ;
public class Hoja4Ejercicio4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner entrada = new Scanner (System.in);
		
		System.out.println("ingrese el numero 1 ");
		int num1 = entrada.nextInt();
		System.out.println("ingrese el numero 1 ");
		int num2 = entrada.nextInt();
		
		
		double  resultado = media(num1,num2);
		
		System.out.println("la media es de " + resultado  );
		
	}
	
	public static double  media  (double  num1 , double num2 )
	{
		
		double  media = ( num1 + num2) / 2 ;
		
	
	  
		return media ; 
		
	}
	
	

}
