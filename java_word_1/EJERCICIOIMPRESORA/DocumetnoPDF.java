package EJERCICIOIMPRESORA;

public class DocumetnoPDF extends Documento {

    
    public DocumetnoPDF(String nombre , String contenido , String tipo){

        super(nombre,contenido,tipo);
    }

    @Override

    public String obtenerFormato(){
         
         return super.obtenerFormato() + " formato pdf ";
    }



     public String toString(){

        return super.toString() + obtenerFormato() ;
    }



    


    
}
