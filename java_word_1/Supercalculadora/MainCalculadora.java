package Supercalculadora;

import java.util.ArrayList;

public class MainCalculadora {

    public static void main(String[] args ){
         
        // Ahora el constructor no necesita parámetros porque los definimos en super()
        Calculadora miCalculadora = new Calculadora();

        // Prueba 1: Sumas simples (Sobrecarga)
        miCalculadora.sumar(10, 5);
        miCalculadora.sumar(20.5, 10.2);

        // Prueba 2: Sumar una lista dinámica (ArrayList)
        ArrayList<Double> listaPrecios = new ArrayList<>();
        listaPrecios.add(100.0);
        listaPrecios.add(50.5);
        listaPrecios.add(25.0);
        
        System.out.println("Procesando lista...");
        miCalculadora.sumar(listaPrecios);

        // Prueba 3: Mostrar historial y métodos heredados
        miCalculadora.mostrarDetalle(); // Viene de Operacion
        miCalculadora.mostrarHistorial(); // Propio de Calculadora

        
    }
    
}
