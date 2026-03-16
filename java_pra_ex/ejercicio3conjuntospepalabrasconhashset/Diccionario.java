package ejercicio3conjuntospepalabrasconhashset;

import java.util.HashSet;

public class Diccionario {
    private HashSet<Palabra> palabras;

    public Diccionario(){
         this.palabras = new HashSet<>();
    }
    
    public boolean AgregarPalabrasSinonimos(Palabra p  ){
            return palabras.add(p);
    }
    public boolean AgregarSinonimosPalabraExistente(String palabra , String sinoagregar ){
       
        for(Palabra p : palabras ){
             if(p.getPalabra().equals(palabra)){
                       p.setSinonimos(sinoagregar);
                       return true ;
             }
        }
        return false ; 
    }

    public void encontrarSinonimosComunes(Palabra a, Palabra b) {   
        HashSet<String> sinonimoA = a.getsinonimos();
        HashSet<String> sinonimoB = b.getsinonimos();
        HashSet<String> comunes = new HashSet<>();
        
        for (String s : sinonimoA) {
            if (sinonimoB.contains(s)) {
                comunes.add(s);
            }
        }
        
        System.out.println("Sinonimos comunes entre '" + a.getPalabra() + "' y '" + b.getPalabra() + "': " + comunes);
    }
    public void mostrarPalabraysinonimos(){
       
        for(Palabra p : palabras ){
             p.toString() ; 
        }
    }

}
