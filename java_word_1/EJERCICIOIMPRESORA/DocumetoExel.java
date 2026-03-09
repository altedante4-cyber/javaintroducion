package EJERCICIOIMPRESORA;

public class DocumetoExel extends  Documento {

    
      
    public DocumetoExel(String nombre , String contenido , String tipo){

        super(nombre,contenido,tipo);
    }




    @Override

    public String obtenerFormato(){
         
         return super.obtenerFormato() + " formato exel";
    }

    public String toString(){

        return super.toString() + obtenerFormato() ;
    }



}

