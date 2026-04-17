import java.io.FileReader;
import java.io.FileWriter;
<<<<<<< HEAD
public class ej9{

public static void main(String[] args){



}

public static void InvierteFicheroInt(String nombre_fichero){
	
	// leemos el primer fichero 
	FileReader leer = new FileReader();
	
	// crear dos archivos
	String positivos = nombre_fichero +positivos;
	String negativos = nombre_fichero + negativos;
	  // escribir en el fichero
        FileWriter escribir_positivos = new FileWriter("positivos");
	FileWriter escribir_negativos = new FileWriter("negativos");

	String valor="";
	int caracter;
	while((caracter = leer.read()) != -1 ){
		char c = (char) caracter;
			
	}	

}
=======
import java.io.IOException;

public class ej9 {
    public static void main(String[] args) {
        SepararFicheroInt("michael");
    }

    public static void SepararFicheroInt(String nombre_fichero) {
        String nombre_positivo = nombre_fichero + "_positivos.txt";
        String nombre_negativo = nombre_fichero + "_negativos.txt";

        try (FileReader leer = new FileReader(nombre_fichero);
             FileWriter escribir_positivo = new FileWriter(nombre_positivo);
             FileWriter escribir_negativo = new FileWriter(nombre_negativo)) {

            String contenido = "";
            int caracter = leer.read();
            while (caracter != -1) {
                contenido = contenido + (char) caracter;
                caracter = leer.read();
            }

            String numero = "";
            for (int i = 0; i < contenido.length(); i++) {
                char c = contenido.charAt(i);

                if (c == '-' || (c >= '0' && c <= '9')) {
                    numero = numero + c;
                } else {
                    if (numero.length() > 0) {
                        if (numero.charAt(0) == '-') {
                            escribir_negativo.write(numero + "\n");
                        } else {
                            escribir_positivo.write(numero + "\n");
                        }
                        numero = "";
                    }
                }
            }

            if (numero.length() > 0) {
                if (numero.charAt(0) == '-') {
                    escribir_negativo.write(numero + "\n");
                } else {
                    escribir_positivo.write(numero + "\n");
                }
            }

            System.out.println("Numeros separados correctamente.");

        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
>>>>>>> 051879a449ea85c9d1e41775e1f527778b3f5475
}
