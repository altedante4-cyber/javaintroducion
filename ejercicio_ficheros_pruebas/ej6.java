import java.util.Scanner ;
import java.io.FileReader;
public class ej6{

	public static void main(String[] argsa){
	
		int caracteranterior=0;
		int caracter = 0 ;
		int contador = 0 ; 
	

	try(FileReader leer = new FileReader("nombres.txt")){
			
			while((caracter = leer.read()) != -1){

				if(caracter == '\n' ){
					contador ++;
				}
				if(caracter == '\n' && caracteranterior == '\n'){
					contador --;
			}
				
				caracteranterior = caracter;
			}
	}catch(Exception e){
		System.out.println(e.getMessage());
	}		

	String nombres [] = new String[contador];
		String name="";
		int posicion = 0 ;
	int caracter_ante= 0;
		int car = 0 ;

	try(FileReader le = new FileReader("nombres.txt")){
		while((car=le.read()) != -1){
			char p = (char) car;

			if(  p != '\n' || caracter_ante != '\n' ){
				name += p ;
			}else {
				nombres[posicion++] = name.trim();
				name = "";
			}

			
			
			caracter_ante = car ;
		}

		if(!name.isEmpty()){
			nombres[posicion]=name.trim();
		}
	
	for(int i = 9 ; i >= 0 ; i --){
		System.out.println(nombres[i]);
	}
	}catch(Exception e ){
		System.out.println(e.getMessage());
	}
	}
}
