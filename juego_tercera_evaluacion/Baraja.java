import java.util.ArrayList;
import java.util.Random;
public class Baraja {

    private ArrayList<Carta> baraja ; 
    
 // preguntar sobre la lista_cartas cuanto tiene que ser el tamnaño y tambien preguntar  sobre como inicialisar 
    public Baraja(){
      
        this.baraja = new ArrayList<>();
    }

    public Baraja(int tipobaraja){
        
        switch (tipobaraja) {
            case 1:
                 
                Carta baraja1  = new Carta(40,10);
                baraja.add(baraja1);


                break;
        
            case 2:
                Carta baraja2 = new Carta(80,0);
                baraja.add(baraja2);
            default:
                break;
        }



    }


    public Baraja(int tipobaraja , boolean barajar1 ){


          switch (tipobaraja) {
            case 1:
                 Carta bajara11= new Carta(40,0);
                if (barajar1){
                     barajar();
                }
        
            case 2;
                Carta baraja2 = new Carta(80,0);

                baraja.add(baraja2);

                if (barajar1){
                    barajar();
                }



            default:
                break;
        }
         
    }

    public void barajar() {
    if (baraja.isEmpty()) {
        System.out.println("No hay cartas en la baraja");
        return;
    }
    
    Random rd = new Random();
    ArrayList<Carta> barajaMezclada = new ArrayList<>();
    int tamanoOriginal = baraja.size();
    
    for (int i = 0; i < tamanoOriginal; i++) {
        int numero = rd.nextInt(baraja.size());
        Carta cartaElegida = baraja.remove(numero);
        barajaMezclada.add(cartaElegida);
    }
    
    this.baraja = barajaMezclada;
}


public void Cortar(int posicion ){

    if(posicion < 0 || posicion > baraja.size() ){ System.out.println("Esa posicion no existe ") ; return ;}

    for(int i = 0 ; i < baraja.size() ; i++){
          Carta mostrar_cartas = baraja.get(i);
          if(i == posicion ){
            break ; 
          }
        System.out.println(mostrar_cartas.toString());
    }

}

public Carta Robar(){

    // tiene que retornar la carta y luego borrarla del array 
    
    Carta devolver = baraja.get(0);
    // borramos la carta
    baraja.remove(devolver);
    return baraja.get(0);
    // aqui estoy teniendo el problema claro tenemos que devolver primero para luego eliminar la carta 
    
}

public void  InsertaCartaFinal(int id_carta){
    Carta carta_intro_id = new Carta(id_carta);
     baraja.add(carta_intro_id);
}

public void InsertaCartaPrincipio(int id_carta ){

     Carta carta_prin_id = new Carta(id_carta);
     ///para isertar valores al principio 
     
     baraja.add(0,carta_prin_id);
}

public void InsertarCartaPrincipio(Carta c ){

    baraja.add(0, c);
     
}

public void InsertaCartaFinal(Carta c ){

    baraja.add(c );
     
}

public int NumeroCartas(){

    return baraja.size();
}

public boolean Vacia(){

    return baraja.isEmpty();
}









    
}
