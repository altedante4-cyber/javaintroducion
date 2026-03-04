public class PruebaLibros {
    public static void main(String[] args ){

         Libro l1 = new Libro("atomicos", "michael", 100, 7);
         Libro l2 = new Libro("ATOM" , "pedro" , 40 , 10);

         ConjuntoLibros cj = new ConjuntoLibros() ;

         if(cj.agregarLibro(l1)){
            System.out.println("Se ha agregado correctamente el libro ");
         }else{
            System.out.println("El libro ya existia pero se agrego correctamente ");
         }

        
         if(cj.agregarLibro(l2)){
            System.out.println("Se ha agregado correctamente el libro ");
         }else{
            System.out.println("El libro ya existia pero se agrego correctamente ");
         }

        

         if(cj.eliminarlibro("atomicos", "michael")){

            System.out.println("el libro ha sido eliminado con exito ");
         }else{
            System.out.println("No se ha podido eliminar el libro ");
         }


        
         if(cj.agregarLibro(l1)){
            System.out.println("Se ha agregado correctamente el libro ");
         }else{
            System.out.println("El libro ya existia pero se agrego correctamente ");
         }

        
        // aqui probamos a introducir un libro que ya existe 


         if(cj.agregarLibro(l1)){
            System.out.println("Se ha agregado correctamente el libro ");
         }else{
            System.out.println("El libro ya existia pero se agrego correctamente ");
         }

        
         
         cj.mostrarelcontenido();

         System.out.println("=========Libros CON MAYOR CALIFICACION ========= ");
         cj.mayorcalificacion();
        
        }
    
}
