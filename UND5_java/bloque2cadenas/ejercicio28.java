import java.util.Scanner ; 
public class ejercicio28 {

    public static void main(String[] args ){

        Scanner sc = new Scanner(System.in);

        String cadena = sc.nextLine();


        String cadena_split [] = cadena.split(" ");


        
        String primer_nombre = cadena_split[0].substring(0,1).toUpperCase();
        String segundo_nombre = cadena_split[1].substring(0,1).toUpperCase();
        

        System.out.println(cadena_split[2] + cadena_split[3] + ","+ primer_nombre +"."+segundo_nombre);


        
         
    }
     
}
