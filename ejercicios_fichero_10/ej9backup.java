import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
public class ej9{
	public static void main(String[] args){
	SepararFicheroInt("michael");
}
public static void SepararFicheroInt(String nombre_fichero){

	String nombre_positivo = nombre_fichero + "positivos";
	String nombre_negativo = nombre_fichero + "negativos";
	int caracter ;
	String acomular_numeros = "";
	try(FileReader leer = new FileReader(nombre_fichero)){


		while((caracter = leer.read()) != -1 ) {
			char c = (char) caracter;
		if ( c == '-' && c >= 48 && c <= 57){
		 	acomular_numeros += c ;	
		}else{
			try(FileWriter escribir_positivo = new FileWriter("nombre_positivo")){
				 escribir_positivo.write(acomular_numeros);
				 acomular_numeros ="";
			}catch(IOException e ) {
				 e.printStackTrace();
			}catch(Exception e){
				System.out.println(e.getMessage());
			}
		}

	}
     }catch(Exception e){
		System.out.println(e.getMessage());
	}
 
 }


}


