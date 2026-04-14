
import java.io.FileWriter;
import java.util.Random ; 
public class ej4 {

public static void main(String[] args){

	EscribeFicheroIntAleatorioPro("ejercicio4.txt" , 10,-5,5);
}

public static void EscribeFicheroIntAleatorioPro(String nombre_archivo , int numero_valores_generar, int valor_minimo  , int valor_maximo){
	Random rd = new Random();
	
	try {
	FileWriter escribir = new FileWriter(nombre_archivo);

	for (int i  = 0 ; i < numero_valores_generar ; i++) {
		int numero = rd.nextInt(valor_minimo,valor_maximo)  ;
		escribir.write(String.valueOf(numero) + "\n" );			
	}
escribir.close();
 }catch(Exception e){

	System.out.println(e.getMessage()) ;
}
}
}
