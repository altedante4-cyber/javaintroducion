package Sistemaderegistrodedispositivos;

import java.util.ArrayList;

public class GestorRed {

     private ArrayList<Dispositivo> listadispositivo = new ArrayList<>();


     public void agregardispositivo(Dispositivo d ){
          listadispositivo.add(d);
     }
     

     public void ejecutarTodos(){
        
        for(int i = 0 ; i < listadispositivo.size() ; i++ ){

              listadispositivo.get(i).realizarAccion();
               
        }

     }


     public ArrayList<Computadora> filtrarPorCOmputadoras(){
         
        ArrayList<Computadora> computadoras  = new ArrayList<>();
         for(int i = 0 ; i < listadispositivo.size() ; i++ ){
              
                    if(listadispositivo.get(i) instanceof Computadora){
                          Computadora comp = (Computadora) listadispositivo.get(i);
                          computadoras.add(comp);
                    }
         }

         return  computadoras ; 
     }





    
}
