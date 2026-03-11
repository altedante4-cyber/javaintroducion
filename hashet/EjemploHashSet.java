import java.util.HashSet;

public class EjemploHashSet {
    public static void main(String[] args) {
        

        HashSet<String> conjuntoFrutas  = new HashSet<String>();


        //ando leemenotss al conjunto 

        conjuntoFrutas.add("pera");
        conjuntoFrutas.add("manzana");
        conjuntoFrutas.add("melon");
        conjuntoFrutas.add("pera");


        // son rapido para ver si un elemenot pertecene al conjunto 

        System.out.println(conjuntoFrutas);
    
       // conceptos sobre la coleccion 
       //  listas : array dinamico importa orden , indexados 
       // conjuntos : es una lista de elemenots no repetidos no import orden si no la perntenencia (existencia  )


       System.out.println(conjuntoFrutas.contains("hola"));
    
    }
    
}
