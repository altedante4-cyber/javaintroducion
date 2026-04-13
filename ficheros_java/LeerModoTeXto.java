import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
public class LeerModoTeXto {
    public static void main(String[] args) {
        
        FileReader entrada;
        int car = 0;
        String cadena ="";
        try {
             entrada=new FileReader("fichero.txt");
            

              while(car != -1 ){ // mientras no sea el final del fichero 
                    car= entrada.read();

                    if(car != 1 )
                        cadena += (char) car + "\n";
              }
              System.out.println(cadena);
              entrada.close();
        } catch (FileNotFoundException e) {
            System.out.println(e.getMessage());
        }catch (IOException e){
             System.out.println(e.getMessage());
        }
    }
    
}
