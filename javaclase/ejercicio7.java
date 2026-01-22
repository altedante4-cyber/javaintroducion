import java.util.Scanner;

public class ejercicio7 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);


        System.out.println("Ingrese el texto ");

        String cadena = sc.nextLine();

        String Char1Str = "";

        while(Char1Str.length() != 1){

             System.out.println("ingrese el primer caracter");

             Char1Str = sc.nextLine();

             if(Char1Str.length() != 1 ){
                System.out.println("Erro vuelve a intentarlo ");
             }
        }

        //solicitamos el segundo numero

        String Char2Str = "";

        while(Char2Str.length() != 1){

            System.out.println("ingrese el segundo numero ");

            Char2Str = sc.nextLine();

            if(Char2Str.length() != 1){

                System.out.println("error ingrese un numero valido ");
            }
        }

        String resultado = "";

        for (int i = 0 ; i < cadena.length() ; i++ ){

            char c = cadena.charAt(i);
            String cStr = "" + c ; 

            if(cStr.equals(Char1Str)){

                resultado += Char2Str;
            }else{

                resultado += cStr ; 
            }
        }

        System.out.println(resultado);

        
        sc.close();

    }
}