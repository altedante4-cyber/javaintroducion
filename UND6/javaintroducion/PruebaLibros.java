package javaintroducion;

public class PruebaLibros {

    public static void main(String[] args){

        Libro miprimerlibro = new Libro("el libro de la saga" , "michael",100 , 5);
        Libro misegLibro = new Libro("padre rico y padre pobre" , "axel" , 5 , 6 ) ;
        

        ConjuntoLIbros basededatos = new ConjuntoLIbros();

        basededatos.agregarlibro(misegLibro);
        basededatos.agregarlibro(miprimerlibro);



        System.out.println(basededatos.toString());
        




        

    }
    
}
