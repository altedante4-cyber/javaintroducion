package javaintroducion;

public class Libro {

    private String titulo , autor;
    private int numero_de_parametros , calificacion;

    //inicialisamos el constructor 

    public Libro(String titulo , String autor , int numero_de_parametros , int calificacion ){
         this.titulo = titulo;
         this.autor = autor ;
         this.numero_de_parametros = numero_de_parametros ;
         this.calificacion = calificacion ; 
    }


 // esto para anadir notas ;
    public boolean anadirlibro(String titulo , String autor, int numero_de_parametros , int calificacion){
            
         this.titulo = titulo ;
         this.autor = autor;
         this.numero_de_parametros = numero_de_parametros;
         this.calificacion = calificacion ;
         return true ; 
    }

    //necesitamos un metodo geter para que nosde el titulo  del libro

    public String dametitulolibro(){
        return  this.titulo;
    }

    // modificar  


    public String nombreuator(){
        return this.autor;
    }

     public int damenumeropaginas(){
        return this.numero_de_parametros;
     }

     public int damecalifacion(){
        return this.calificacion;
     }


     public void eliminartitulo(Libro f){

         f = null ; 
    }




}
