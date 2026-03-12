import java.util.ArrayList;
import java.util.Random;
public class Baraja {

    private ArrayList<Carta> baraja ; 


    public Baraja(){
    
            baraja  = new ArrayList<>();

    }

    public Baraja(int tipobaraja){
        
        switch (tipobaraja) {
            case 1:
                 
                 Carta bajara11= new Carta(40,0);
                
                break;
        
            case 2;
                Carta baraja2 = new Carta(80,0);
            default:
                break;
        }



    }


    public Baraja(int tipobaraja , boolean barajar ){


          switch (tipobaraja) {
            case 1:
                 
                 Carta bajara11= new Carta(40,0);
                                
                break;
        
            case 2;
                Carta baraja2 = new Carta(80,0);
            default:
                break;
        }
         
    }

    public void Barajar(){

        Random rd = new Random();
        int obtener_carta = rd.nextInt(baraja.size());
        // esto teva a devolver un objeto carta y ese objeto carta 

        Carta n 0 baraja[obtener_carta];

    }
        
    }
    
}
