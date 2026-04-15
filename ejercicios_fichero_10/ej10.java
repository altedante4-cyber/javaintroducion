import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
public class ej10 {
    public static void main(String[] args) {
        InvierteFicheroint("ejercicio10.txt");
    }
    public static void InvierteFicheroint(String nombre_fichero) {

 	ArrayList<Character>letras = new ArrayList<>(); 
      try (FileReader fl = new FileReader(nombre_fichero)) {
            for (int caracter = fl.read()  ; caracter != -1; caracter = fl.read()) {
                 letras.add((char)caracter);
            }
			FileWriter escribir = new FileWriter(nombre_fichero);

	for(int i = letras.size() -1 ; i >= 0 ; i--){
		escribir.write(letras.get(i));
	}	
	escribir.close();


        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
