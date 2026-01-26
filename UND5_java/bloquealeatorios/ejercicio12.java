package bloquealeatorios;
import java.util.Random;
public class ejercicio12 {
    public static void main(String[] args ){

            Random num = new Random();

    boolean soniguales = false;
    int dados [] = new int[2];

    while(!soniguales){
         
        for(int i = 0 ; i < 2 ; i ++ ){

              int dado = num.nextInt(6) + 1;

              dados[i] = dado;
        }

        if (dados[0] == dados[1]){
              soniguales = true;             
        }
    }
    System.out.println(dados[0]);
    System.out.println(dados[1]);

    }
}
