package Juego2eva;

public class probarfracion {

    
    public static void main(String[] args ){


        Fraccion f1 = new Fraccion(5, 2);
        Fraccion f2 = new Fraccion(2,3);

        System.out.println(f1 + "+" + f2 + "== " + f1.sumarFraccion(f2));

        System.out.println(f1 + "+" + f2 + "== " + f1.diviFraccion(f2));

        System.out.println(f1 + "+" + f2 + "== " + f1.restaFraccion(f2));

    }
}
