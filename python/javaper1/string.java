public class string {

    public static  void main (String [] args){

        //Cadenas de texto

        String name = "michael";
        var surname = new String(name);  // estos es el constructo  del string
        // CONCATENACION

        IO.println( name + " " + surname);
        // hayar la longitud con length

        //hayar lka long tud de name
        IO.println(name.length()); // con esto sabemos la longitud  del string


        //charAT
        //obterner caracteres

        IO.println(name.charAt(1));

        // este es otra manera de hacerlo

        IO.println(name.charAt(name.length() - 1 )); // con esto no necesitamos saber cuantos caracteres tiene el string esto nos devolvera  un caracter le estamos diciendo  la cantidad de carcteres menos 1

     // si queremos obtener una subcadena

        IO.println(name.substring( 2 )); // esto quiere decir que empiese a sacaqr desde el numero 2 del string

        IO.println(name.substring(1,3)); // con esto le decimos que empiese desde el 1 y termine en el 3

        // nos permite cambiar la cadena de texto en todo mauscula o todo minuscula

        IO.println(name.toUpperCase());
        IO.println(name.toLowerCase());

        name = name.toUpperCase(); // con esto lo queremos decir que  el nuevo valor del


        IO.println(name);

 //COMPROBAR SI CONTIENE ALGO
        IO.println("hola , java".contains("Michael")); // en este caso nos da false por que tiene que tener la misma cadena de caracteres para que sea true
        IO.println("hola,java".toUpperCase().contains("AVA")); // ahora nos da true por que  hola  java se convierte en mayuscula   y conincide con

        // equals => como conpar si una codnea de tesxto es igual a otra cadena de textoo

    }
}
