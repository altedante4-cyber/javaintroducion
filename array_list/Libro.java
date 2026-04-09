public class Libro {

    private String titulo , autor ;
    private int numero_paginas , calificacion ;


    public Libro(String titulo, String autor , int numero_paginas , int  califcacion ){

         this.titulo = titulo ;
         this.autor = autor;
         this.numero_paginas = numero_paginas ;
         try{
             validarcalificacion(califcacion);
             
         }catch(ValidarRango a ){
            System.out.println(a.getMessage());
             
         }
    }



    public void validarcalificacion(int califcacion) throws ValidarRango {
    
          if( 0 < califcacion  ||   califcacion > 10){
            throw new ValidarRango("No se pudoo introducir ");
            
        }

        this.calificacion = califcacion ; 
    }

    public String getTitulo(){
        return titulo ; 
    }
    public String getautor(){
        return autor ; 
    }

    public int getcalifcacion(){
        return calificacion  ; 
    }



 public String toString(){

    return "El libro " + titulo + "autor " + autor + " su numero de paginas es  " + numero_paginas + " y su nota es " + calificacion ;  
 }


    
}
