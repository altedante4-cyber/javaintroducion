import java.io.FileReader;
import java.io.FileWriter;
import java.util.Scanner ; 
public class ej1{

	public static void main(String[] args){
			Scanner sc = new  Scanner(System.in);
		 System.out.println("introduce nombre archivo");
		 String nombre = sc.nextLine();
		try(FileReader leer = new FileReader(nombre)){
			int caracter;
			int contador_lineas = 0 ;
			while((caracter = leer.read()) != -1 ){
				char c = (char) caracter;
				if( c == '\n'){
					contador_lineas ++;
				}
			}
			leer.close();
		System.out.println(contador_lineas);

		}catch(Exception e){
			System.out.println(e.getMessage());
		}
	}
}
