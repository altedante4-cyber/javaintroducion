package bloquealeatorios;

import java.util.Random;

public class ejercicio3 {
        
    static Random num = new Random(); 
     public static void main(String[] args ){
        String palos [] = {"picas","corazones","diamantes" , "treboles"};
        // aqui me equivo por que queria almacenar los numeros  en un char pero el char solo permite almacenar 1 numero 

        int n = num.nextInt(13) + 1 ;
        String valor = "";

        if ( n == 1){
            valor += "A";
        }else if ( n == 10){
            valor += "J";
        }else if (n == 11){
             valor += "Q";
        }else if (n == 12 ){
             valor += "K";
        }else{

            valor += String.valueOf(n);

        }

        System.out.println(generarcarta(palos) +" " + valor);

        

        

        


     }

     public static String generarcarta(String a []){

           int generar_palabra = num.nextInt(a.length );


           return a[generar_palabra] ;
           
    }
    

}
