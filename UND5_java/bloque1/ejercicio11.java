package bloque1;
import java.util.Random;

public class ejercicio11 {
    public static void main(String[] args){

        Random notas_generadas = new Random();

        String notas [] = {"suspenso","suficiente","bien","notable","sobresaliente"};
        
        String notas_generadas_aleatorias [] = new String[20];

        for (int i = 0 ; i < 20 ; i++ ){

            int generar =notas_generadas.nextInt(notas.length);

            notas_generadas_aleatorias[i] = notas[generar];
        }

    
        int contador_suspensos = 0;
        int contador_bien = 0;
        int contador_notable = 0 ;
        int contador_sobresaliente = 0 ;

        for (int i = 0 ; i < notas_generadas_aleatorias.length ; i++ ){

            if (notas_generadas_aleatorias[i].equals("suspenso")){
                contador_suspensos += 1 ;
            }else if (notas_generadas_aleatorias[i].equals("bien")){
                contador_bien += 1;
            }else if (notas_generadas_aleatorias[i].equals("notable")){
                contador_notable += 1;
            }else if (notas_generadas_aleatorias[i].equals("sobresaliente")){
                contador_sobresaliente += 1;
            }
        

            
    }

        System.out.println(contador_suspensos);
     System.out.println(contador_bien);
     System.out.println(contador_sobresaliente);
     System.out.println(contador_notable);



    }

    
}
