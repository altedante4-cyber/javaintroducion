package Listadecontactos;

public class Maincontactos {

    public static void main(String[] args ){
        
        Contacto nuevos_contactos = new Contacto();


         nuevos_contactos.agregarContacto("michael");
         nuevos_contactos.agregarContacto("aguilar");
         nuevos_contactos.agregarContacto("peredo");
         nuevos_contactos.agregarContacto("axel");

         if(nuevos_contactos.buscarContacto("aguilar")){
            System.out.println("encontrado");
         }else{
            System.out.println("No encontrado");
         }

         if(nuevos_contactos.eliminarConctato("michael")){
            System.out.println("Usuario eliminado ");
         }else{
            System.out.println("No ha sido eliminado por que no  ha sido encontradoa ") ;
         }
         nuevos_contactos.mostrarContactos();

    }
    
}
