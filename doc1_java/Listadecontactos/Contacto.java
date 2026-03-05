package Listadecontactos;

import java.util.ArrayList;

public class Contacto {

    private String nombre ; 
    private ArrayList<String> lista_contactos = new ArrayList<>()  ; 

    

    public boolean agregarContacto(String nombre ){
        // forma mas limpia para confimar
        return lista_contactos.add(nombre);

        // por que es mejor asi

        /* legibilidad menor lineas de codigo mas direcot al grano 
        eficiencia te ahoras uan evaluacion logica innecesaria
         */


    }

    public boolean eliminarConctato(String nombre ){

         // primero hay que asegurarnos que existe ese nombre el remove devuelve un boolean es decir no hace falta buscar  por que si no lo encuentra es que no esta

         return lista_contactos.remove(nombre);
    }


    public void mostrarContactos(){

        for (int i = 0 ; i < lista_contactos.size() ; i++ ){

             // el get de ayuda a sacar los datos del array 

             String contacto = lista_contactos.get(i);
l ){
             System.out.println(i + " contacto => " + contacto );
            // validacion del null es innecesaria por que dond etu controlas la entrada es muy raro que existan elemenos nulos
            // a menos que tu los anadiddas a proporito puedes quitar ese if par a 


        }
    }

    public boolean buscarContacto(String nombre ){

         return lista_contactos.contains(nombre);
    }


}