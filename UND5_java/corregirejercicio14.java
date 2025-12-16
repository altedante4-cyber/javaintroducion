import java.util.Scanner ; 
import java.util.Random;
public class corregirejercicio14 {
	public static void main(String[] args) {
		Random genAle = new Random();
		
		
		int numCompases  = genAle.nextInt(6)+1;
		
		String melodia = "";
		
		boolean ultimoCompas = false;
		
		for (int i = 0 ;  i < numCompases ; i++) {
			
			if(i ==numCompases - 1 ) {
				ultimoCompas = true ; 
				melodia = generarCompar(melodia,ultimoCompas);
			}
			
			
		}
		
		melodia += "|";
		
		System.out.println(melodia);
		
	}
	
	public static String generarCompar(String melodia,boolean ultimoCompas ) {
		
			Random genAle = new Random();
			
			String [] notas = {"do","re","mi","fa","sol","la","si"};
			
			for (int i = 0 ; i < 4 ; i ++ ) {
				
				int numAle = genAle.nextInt(7);
				
				melodia = melodia + " "+notas[numAle] + " ";
			}
			
			melodia += "|";
			
			return melodia ;
			
		
	}
	
	public static String extraerPrimeraNota(melodia) {
		String primeraNota = "";
		
		for (int i = 0 ; i <melodia.length ; i ++ ) {
			
			if(melodia.charAt(i) != ' ')
				primeraNota = melodia.charAt(i);

		}
					
		
		
	}

}
