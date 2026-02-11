package Juego2eva;
import java.util.Scanner ; 
public class probarfracion {

    
    public static void main(String[] args ){

        Scanner scanner = new Scanner(System.in);
        System.out.println("Introduce numerador f1 : ");

        int n = scanner.nextInt();
        System.out.println("Introudce denominador f1: ");
        int d scanner.nextInt();

        Fraccion f1 = new Fraccion(n,d);


        System.out.println("Introduce numerador y denominador f2");

        Fraccion f2 = new Fraccion(scanner.nextInt(), scanner.nextInt());


        System.out.println(f1 + "x" + f2+"=" + f1.multFraccion(f2));

        

    }
}
