package bloquealeatorios;
import java.util.Random;
public class ejercicio11 {
    public static void main(String[] args){
        Random num = new Random();
        String nota = "";
        int contador_suspensos = 0 ;
        int contador_suficiente = 0 ;
        int contador_bien = 0 ;
        int contador_notable = 0 ;
        int contador_sobresaliente = 0 ; 

    for(int i = 0 ; i < 20 ; i++ ){

         int notas = num.nextInt(11);

         if(notas >= 0 && notas < 5 ){
              nota += "suspenso\n";
             contador_suspensos ++;
            }else if(notas >= 5 && notas < 8 ){
             nota += "suficiente\n";
             contador_suficiente ++;
         }else if (notas == 8 ){
            nota += "bien\n";
            contador_bien ++;
         }else if (notas == 9){
            nota += "notable\n" ;
            contador_notable ++;
         }else {
             nota += "sobresaliente\n";
            contador_sobresaliente ++;
            }

    }
     
    System.out.println("=================RESULTADO=========================");
    System.out.println("Suspensos salio un total de " + contador_suspensos);
    System.out.println("Suficientes salio un total " + contador_suficiente);
    System.out.println("Notas bien " + contador_bien);
    System.out.println("Notas notables" + contador_notable);
    System.out.println("Notas sobresaliente " + contador_sobresaliente);
    System.out.println(nota );


    }
   
}
