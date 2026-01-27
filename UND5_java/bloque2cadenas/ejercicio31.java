public class ejercicio31 {

    public static void main(String[] args){
         
          String cadena = " hola peredo ";
String cadena_nueva = cadena.replaceFirst("^\\s+", "");
System.out.println(cadena_nueva);  // "hola peredo "

    }
}
