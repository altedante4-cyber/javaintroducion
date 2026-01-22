import java.util.Scanner ; 
public class ejercicio8 {

    public static void main(String [] args ){

        Scanner sc = new Scanner (System.in);
       System.out.println("ingrese la cadana ");

       String cadena = sc.nextLine();
       String resultado = "";

       for (int i = 0 ; i < cadena.length() ; i++ ){

            char c = cadena.charAt(i);

            String Cstr = "" + c;

            String minuscula = convertirMinuscula(Cstr);
            String mayuscula = convertirMayuscula(Cstr);
            if(!minuscula.equals(Cstr)){
                //si el caracter convertido a minuscula es diferentre del original
                resultado += minuscula;
            }else{
                resultado += mayuscula ;
            }
       }

       

       System.out.println(resultado);

    }

    public static String convertirMinuscula(String letra){

        return letra.toLowerCase();
    }

    public static String convertirMayuscula(String letra){

        return letra.toUpperCase();
    }
    
}
