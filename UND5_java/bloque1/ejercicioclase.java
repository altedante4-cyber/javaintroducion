package bloque1;
import java.util.Random;
public class ejercicioclase {

    public static void main(String[] args ){

         Random num = new Random();

         int numeros [] = new int[10];


         for(int i   = 0 ; i < 10 ; i ++ ){
                
             numeros[i] = num.nextInt(0,100+1);

         }

        int contadorpares = 0 ;
        int contadorinpares = 0 ;

        for(int j = 0 ; j < numeros.length ; j++ ){
             if(numeros[j] % 2 == 0 ){

                contadorpares++ ;
             }else{
                contadorinpares ++;
             }
        }

        int numeros_mayor = numeros[0];
        int numeros_menor = numeros[0];


        for(int i = 0 ; i < numeros.length ; i++ ){
             if(numeros[i] > numeros_mayor){
                numeros_mayor = numeros[i];
             }else{
                numeros_menor = numeros[i];
             }
        }
        int contador_numeros = 0 ; 

        for(int i = 0 ; i < numeros.length ; i++ ){

            contador_numeros += numeros[i];
        }

        double media = (double) contador_numeros / numeros.length ; 

        int datos_pares [] = new int[contadorpares];
        int datos_inpares [] = new int[contadorinpares];

        for(int i = 0 ; i < numeros.length ; i++ ){
            if (numeros[i] % 2 == 0 ){
                datos_pares[i] = numeros[i];
            }else{
                datos_inpares[i] = numeros[i];
            }
        }

        int caculo_mediana_inpares = datos_inpares.length / 2 ;
        int calculo_media_pares = datos_pares.length / 2  ;

        System.out.println(caculo_mediana_inpares);
        System.out.println(calculo_media_pares);




        }
    
}
