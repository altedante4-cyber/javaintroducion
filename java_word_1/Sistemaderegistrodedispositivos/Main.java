package Sistemaderegistrodedispositivos;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args ){
         
         GestorRed disp = new GestorRed();

         Computadora cp1 = new Computadora("mac", "2034", "linux");
         Router r1 = new Router("MOVISTAR", "1256", "ubuntu", 20);
    
    
        disp.agregardispositivo(cp1);
        disp.agregardispositivo(r1);
    
        disp.ejecutarTodos();

        ArrayList<Computadora> comp = disp.filtrarPorCOmputadoras();


        for(int i = 0 ; i < comp.size() ; i++ ){
             System.out.println(comp.get(i));
        }
        
    }
    
}
