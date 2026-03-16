package ejercicio3conjuntospepalabrasconhashset;

import java.util.HashSet;

public class Palabra {
    private String palabra;
    private HashSet<String> sinonimos;

    public Palabra(String palabra , HashSet<String> sinonimos  ){
        this.palabra=palabra;
        this.sinonimos = sinonimos;
    }
    public String getPalabra(){
         return palabra;
    }
    public HashSet<String> getsinonimos () {
        return sinonimos;
    }

    public void setSinonimos( String palabra ){
          
          this.sinonimos.add(palabra);
    }
  
    public String toString(){

         return "Palabra | " + palabra + sinonimos ; 
    }
    
}
