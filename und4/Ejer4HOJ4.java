package und4;


import java.util.Scanner ; 
public class Ejer4HOJ4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		// QUE LEA 5 NUMEROS PRO TECLADO LOS COPIA A OTRO ARRAY MULTIPLICOS POR 2 Y MUESTRE EL SEGUNDO ARRAY
		
		// aqui solo me falta hacer otro bucle que introdusca primero esos numeros a un array y luego recien los pasea otor array multiplicado por 2 
		
		Scanner entrada = new Scanner(System.in);
		
		
		
		int [] num3 = new int [5];
		int [] num = new int [5];
		
		
		for (int i =0 ; i <= 4; i++ ) {
			
			System.out.println("ingrese numero"  + i );
			
			int num2 = entrada.nextInt();
			
			num3[i] += num2;
			
		}
		
		
		for(int num5 : num ) System.out.print(num3 + " ");
		
		
		
		
		
		

	}

}
