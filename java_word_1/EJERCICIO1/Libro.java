public class Libro{

    private String titulo ;
    private String autor ;
    private int anioPublicacion ;
    private boolean disponible ; 


    public Libro(String titulo , String autor , int anioPublicacion ){
        this.titulo = titulo ;
        this.autor = autor ;
        this.anioPublicacion = anioPublicacion  ;
        this.disponible = true ; 
    }


    public boolean prestar(){
        if(disponible) { disponible = false ;  return true ; }; 
        return false ; 
    }
    public boolean devolver(){
         return disponible = true ; 
    }
    public void mostrarInfo(){
        System.out.println("Nombre del libro " + titulo  + "auto es " + autor + " el anio de publicacion es  " + anioPublicacion );
    }



}