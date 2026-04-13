import java.io.FileWriter;
public class EscribirModoTexto {
    public static void main(String[] args) {
    FileWriter salida ;
    try {

        //creo el canal 
    salida=new FileWriter("fichero.txt");
        for(int i = 0 ; i < 10 ; i++){
             salida.write(i + "\n");
        }

        // cuando ya no lo voy a usar cierro el canal 
        salida.close();
    } catch (Exception e) {
        System.out.println(e.getMessage());
    }
    }    
}
