
import java.io.FileWriter;
import java.util.Random;
import java.text.FieldPosition;
public class ej3 {

    public static void main(String[] args) {
        	EscribeFicheroIntALeatorio("ejercicio3.txt",10);
    }

    public static void EscribeFicheroIntALeatorio(String nombre_archivo,int cuantos_numeros_aleatorios ){
	Random rd = new Random();
        try{
		 FileWriter escribir = new FileWriter(nombre_archivo);
        	for (int i = 0 ; i < cuantos_numeros_aleatorios ; i++){
			  	int numero = rd.nextInt(1,100);
				escribir.write(String.valueOf(numero)) ;
        	 }
	escribir.close();
	
       }catch(Exception e ) {
	System.out.println(e.getMessage()) ; 
  } 
	 
    }
    
}
