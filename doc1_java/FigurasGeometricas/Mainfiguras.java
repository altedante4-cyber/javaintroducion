package FigurasGeometricas;

import java.util.ArrayList;

public class Mainfiguras {
    public static void main(String[] args ){

        ArrayList<Figura> figuras = new ArrayList<>();

        Circulo c1 = new Circulo(10);
        Rectangulo r1 = new Rectangulo(10, 5);
        Triangulo t1 =  new Triangulo(10, 5, 2, 3, 4);


        figuras.add(c1);
        figuras.add(r1);
        figuras.add(t1);

        for(int i = 0 ; i< figuras.size() ; i++ ){

               Figura p = figuras.get(i);

               System.out.println(p.toString());
               
        }
    }
}
