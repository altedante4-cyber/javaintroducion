package EJERCICIOIMPRESORA;

public class Documento {

    
    private String nombre ;
    private String contenido ;
    private String tipo ;


    public Documento(String nombre , String contenido , String tipo) {

          this.nombre = nombre ;
          this.contenido = contenido;
          this.tipo = tipo ;  
    }

    public String  obtenerFormato(){

        String imprimir = "-------------------imprimir-------------";

        return imprimir ;
    }



    public String toString(){
         return "Nombre " + nombre + "el contenido " + contenido  + "el tipo es " + tipo ;   
    }





}
