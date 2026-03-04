import java.util.ArrayList;

public class ConjuntoLibros {
    
    ArrayList <Libro> libros = new ArrayList<>();

    public boolean  agregarLibro(Libro l ){
        // funcionalidad para agregar un libro que ya existe

        if(!libros.contains(l)){
            libros.add(l);
            return true ; 
        }

        libros.add(l);
     return false ; 

    }
    public boolean eliminarlibro(String titulo , String autor  ){
        

        for (int i = 0  ; i < libros.size() ; i++ ){
            
                Libro lo = libros.get(i);
                
                if (lo.getTitulo().equals(titulo) && lo.getautor().equals(autor)){
                    
                    libros.remove(lo);
                    return true ; 
                }
                
        }

                return false  ; 
        
    }

    public  void mayorcalificacion(){


        for (int i = 0 ; i< libros.size() ; i++ ){

                Libro l = libros.get(i);
                
                if ( l.getcalifcacion() >= 8 ){
                    System.out.println(l);
                }
        }
         

    }


    public void mostrarelcontenido(){

        for(int  i = 0 ; i< libros.size() ; i++ ){

            Libro l = libros.get(i);

            System.out.println(l);
        }
    }



}
