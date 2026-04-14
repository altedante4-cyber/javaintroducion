import java.io.FileWriter;
import java.io.IOException;
public class ej1 {
    public static void main(String[] args) {
            EscribirFichero1_100("hola.txt");

    }

    public static  void EscribirFichero1_100(String nombre_fichero){
    

        try {
        FileWriter escribir = new FileWriter(nombre_fichero);
         
        for (int i = 1 ; i < 100 ; i++ ){
             escribir.write(String.valueOf(i)); 

        }
         escribir.close();   

        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
    
}
