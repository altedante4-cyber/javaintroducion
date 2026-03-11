import java.util.ArrayList;

public class Baraja {

    private ArrayList<Carta> cartas  ; 


    public Baraja(){
    
            cartas = new ArrayList<>():

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
                 if barajar:
                    Barajar();                
                break;
        
            case 2;
                Carta baraja2 = new Carta(80,0);
            default:
                break;
        }
         
    }

    public void Barajar(){

         
    }
    
}
