public class Libro {

    private String titulo , autor ;
    private int numero_paginas , calificacion ;
    public Libro(String titulo, String autor , int numero_paginas , int  calificacion ){
         this.titulo = titulo ;
         this.autor = autor;
         this.numero_paginas = numero_paginas ;
         try{
             validarcalificacion(calificacion);   
         }catch(ValidarRango a ){
            System.out.println(a.getMessage());     
         }
    }



    public void validarcalificacion(int calificacion) throws ValidarRango {
    
        if( calificacion < 0  ||   calificacion > 10){
            throw new ValidarRango("No se pudoo introducir ");
            
        }
            this.calificacion = calificacion ; 

        

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

public class Libro {

    private String titulo, autor;
    private int numero_paginas, calificacion;

    // Agregamos 'throws' para que quien cree el libro sepa que puede fallar
    public Libro(String titulo, String autor, int numero_paginas, int calificacion) throws ValidarRango {
        this.titulo = titulo;
        this.autor = autor;
        this.numero_paginas = numero_paginas;
        // Validamos antes de asignar
        validarcalificacion(calificacion);
    }

    public void validarcalificacion(int calificacion) throws ValidarRango {
        // CORRECCIÓN: Si es menor a 0 O mayor a 10, es error
        if (calificacion < 0 || calificacion > 10) {
            throw new ValidarRango("Error: La calificación " + calificacion + " no es válida.");
        }
        this.calificacion = calificacion;
    }

    // Getters y toString...
    public String toString() {
        return "El libro " + titulo + " de " + autor + " tiene " + numero_paginas + " páginas y una nota de " + calificacion;
    }
}