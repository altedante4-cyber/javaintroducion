package Sistemadevideoclub;

public class Pelicula {
    
    //equivocaciones que voy teniendo es 
    // 1 . al construir el constructor  en validaranio no hace falta poner delante el this por que en el void de abajo ya se hace
    private String titulo , director  ;
    private int anio ;
    private boolean disponible ; 

    // getter /setters con validacion del ano tostring

    public Pelicula(String titulo , String director , int anio ){

        this.titulo = titulo ;
        this.director = director;
        validaranio(anio);
        this.disponible = true ;
    }

    

    //validar anio 

    public void validaranio(int anio ){

        if(anio < 0 ){

            this.anio = 0 ; 

        }

        this.anio = anio ; 
    }


    public boolean estaLibrePelicula(){
        return disponible ;
    }

    public String dametitulo(){
        return titulo ; 
    }


}
