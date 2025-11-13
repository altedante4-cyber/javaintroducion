package und4;

import java.util.Scanner;
public class CorrecionEjercicio4Hoja4 {

	public static void main(String[] args) {
		
		Scanner entrada = new Scanner (System.in);
		System.out.println("introudce dos numeros ");
		int num1 = entrada.nextInt();
		int num2 = entrada.nextInt();
		
		double media = media(num1 ,num2);
		System.out.println(media);
		
	}
	
	public static double media (int a , int b ) {
		
		double  rsdo = (double)(a+b) / 2 ;
		
		return rsdo ; 
	}

}
