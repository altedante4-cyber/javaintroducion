package bloque1;

import java.util.Scanner ;
import java.util.Random;
public class ejercicio15 {
static   Random elegir_numero = new Random();

    public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    String figuras [] = {"corazon","diamante","herradura","campana","limon"};

    String guardar_figuras [] = new String[3];
 for (int i = 0  ; i < 3 ; i++ ){
    String palabrajugar = palabra_elegida(figuras);

      guardar_figuras[i] = palabrajugar;
    
 }

 String   a = "";
 String b = "";
 String c = "";
for (int i = 0 ; i < guardar_figuras.length ; i++ ){
    
     if (i == 0 ){
      a += guardar_figuras[0];

     }else if (i == 1){
    b += guardar_figuras[1];
     }else if (i == 2){
      c += guardar_figuras[2];

      }


    }


    if(a.equals(b) && a.equals(c)){
        System.out.println("Enhorabuena,ha ganado 10 monedas");
    }else if(a.equals(b) && !a.equals(c)){
        System.out.println("Bien,ha recuperado su moneda");
    }else if(a.equals(c) && !a.equals(b)){
        System.out.println("Bien,ha recueprado su moneda");
    }//hay que hacer lo mismo ahora para todoso
    else if(b.equals(c) && b.equals(a)){
        System.out.println("Enhorabuena,ha ganado 10 monedas");
    }else if(b.equals(c) && !b.equals(a)){
        System.out.println("Bien , ha recuperado su moneda");
    }else if(b.equals(a) && !b.equals(c)){
        System.out.println("Bien,ha recuperado su moneda");
    }
    else if(c.equals(a) && c.equals(b)){
        System.out.println("Enhorabuena,ha ganado 10 monedas");
    }else if (c.equals(a) && !c.equals(b)){
        System.out.println("Bien, ha recueprado su moneda");
    }else if (c.equals(b) && !c.equals(a)){
        System.out.println("Bien,ha recuperado su moneda");
    }else{
        System.out.println("Lo siento, ha perdido");
    }

    System.out.println(a);
    System.out.println(b);
    System.out.println(c);
    
}   
public static String palabra_elegida(String a []){

    int numero = elegir_numero.nextInt(a.length);

    String palabra_legida = a[numero];

    return palabra_legida;


     
}



}
