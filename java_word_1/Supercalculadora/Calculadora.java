package Supercalculadora;

import java.util.ArrayList;
public class Calculadora extends Operacion {

    private ArrayList<String> historial ;
    
    public Calculadora() {
        // al padre le enviamos datos inicales para que el objeto se cree correctamente
        super("calcula pro" , 0.0, "05/01/0130");
        this.historial = new ArrayList<>();
    }

    // sobrecarga 1 enteros

    public void sumar(int a , int b ){
         
         int res = a  + b ;

         historial.add("suma enteros " + a + " + " + b + " = " + res 
         );
    }


    // sobrevcarga 2 decimales 

    public void sumar(double a , double b ) {

         double res = a + b ;
         historial.add("suma decimales "+ a + " + " + b + " = " + res );
    }
    

    // sobrecarga 3 arraylist polimorfimmo con colecciones

    public double sumar(ArrayList<Double> numeros ){
         double total = 0 ;
         
         for (Double num : numeros ){
             if (num != null ) total += num;

         }
         historial.add("suma de lista : total " + total );
         return total ; 
        }

        public void mostrarHistorial(){
             System.out.println("====HISTORIAL DE LA CALCULADORA");

             for(String registro : historial ){
                System.out.println("--" + registro);
             }
        }
}
