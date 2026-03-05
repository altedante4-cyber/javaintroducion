package Ejercicio4;

public class MainElectrodomestico {
    public static void main(String[] args ){

        Electrodomestico [] electrodomesticos = new Electrodomestico[10];

        Lavadora l1 = new Lavadora(10, "blanco", 'A', 20, 20);
        Television t1 = new Television(10, 20);


        electrodomesticos[0]=l1 ; 
        electrodomesticos[1] = t1 ; 


        for (int i = 0 ; i < electrodomesticos.length ; i++ ){
             
               if(electrodomesticos[i] != null ){
                System.out.println(electrodomesticos[i].toString());
               }
        }

    }
    
}
