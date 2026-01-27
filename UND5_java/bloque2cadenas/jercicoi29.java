import java.util.Scanner ; 
public class jercicoi29 {

    public static void main(String[] args ){

        Scanner sc = new Scanner(System.in);

        String cadena = sc.nextLine();
        char b = sc.nextLine().charAt(0);
        int contador = 0 ; 

        for(int i = 0 ; i < cadena.length() ; i++ ){

               char c = cadena.charAt(i);

               if(b == c    ){
                    contador ++;
               }
        }

         
        System.out.println(contador);
    }
    
}
