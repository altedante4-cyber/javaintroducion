package EJERCICIOIMPRESORA;

public class Impresora {
    


    public void imprimir(Documento d ){
         
         System.out.println(d.toString());
    }

    public void imprimir(String texto  ){
         
         System.out.println("esto no es una nota formal ");
    }
 
 
   public void imprimir(String [] lineas  ){
        // recibe una lista de frase y los va imprimiendo una por una 

        for (int i = 0 ; i < lineas.length ; i++ ){

              System.out.println( i + "lineas " + lineas[i]);
        }


    }
    public void imprimirInforme(Documento[] listaDocumentos ){
    
    for(int i = 0  ; i < listaDocumentos.length ; i++ ){
         
          System.out.println(listaDocumentos[i].toString());
    }
}

    
    

    

    

}
