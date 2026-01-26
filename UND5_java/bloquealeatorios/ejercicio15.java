package bloquealeatorios;
import java.util.Random;
public class ejercicio15 {
    
    public static void main(String[] args ){
         Random num = new Random();

         String figuras[] = {"Corazon","diamante","herradura","Campana","limon"};
         String mostrarfiguras [] = new String[3];


         for(int i =0 ;i < 3 ; i++ ){

              int elegir = num.nextInt(figuras.length);
              String palabra = figuras[elegir];
              mostrarfiguras[i] = palabra;
         }

         System.out.println(mostrarfiguras[0]);
         System.out.println(mostrarfiguras[1]);
         System.out.println(mostrarfiguras[2]);
         

         if(mostrarfiguras[0].equals(mostrarfiguras[1]) && mostrarfiguras[1].equals(mostrarfiguras[2])){
             System.out.println("Son todos iguales");
         }else if (mostrarfiguras[0].equals(mostrarfiguras[1]) || mostrarfiguras[0].equals(mostrarfiguras[2]) || mostrarfiguras[1].equals(mostrarfiguras[2])){
            System.out.println("Son dos iguales y uno distinto ");
         }else{
            System.out.println("Son todos distintos ");
         }
         
    }
}
