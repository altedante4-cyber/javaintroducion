package bloquealeatorios;
import java.util.Random;
public class ejercicio10 {
    public static void main(String[] args ){

        Random numeros = new Random();

        char caracters [] = {'*','|','#','@','-','='};

        for(int i = 0 ; i < 10 ; i++ ){
             
             int bloque = numeros.nextInt(40)+ 1 ; 
             for(int j = 0 ; j < bloque ; j++ ){
                  
                   int caracter = numeros.nextInt(caracters.length);
                   System.out.print(caracters[caracter]);
             }

             System.out.println();
        }
         
    }
    
}
