package bloquealeatorios;
import java.util.Random ;  
public class ejercicio19 {
    public static void main(String[] args ){

         Random  num = new Random() ;

         for(int i = 0 ; i < 5 ; i++ ){

               int vocal = num.nextInt(26)+97;
               char c = (char) vocal ;

               System.out.print(c);
         }
    }
}
