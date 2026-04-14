import java.util.ArrayList;
import java.util.Random;

public class Baraja {

    private ArrayList<Carta> lista_cartas;

    public Baraja() {
        this.lista_cartas = new ArrayList<>();
    }

    public Baraja(int tipobaraja) {
        this.lista_cartas = new ArrayList<>();
        switch (tipobaraja) {
            case 1:
                for (int i = 1; i <= 40; i++) {
                    lista_cartas.add(new Carta(i));
                }
                break;
            case 2:
                for (int i = 1; i <= 80; i++) {
                    lista_cartas.add(new Carta(i));
                }
                break;
        }
    }

    public Baraja(int tipobaraja, boolean barajar) {
        this.lista_cartas = new ArrayList<>();
        switch (tipobaraja) {
            case 1:
                for (int i = 1; i <= 40; i++) {
                    lista_cartas.add(new Carta(i));
                }
                break;
            case 2:
                for (int i = 1; i <= 80; i++) {
                    lista_cartas.add(new Carta(i));
                }
                break;

    
        }
        if (!lista_cartas.isEmpty() && barajar) {
            barajar();
        }
    }

    public void barajar() {
        Random rand = new Random();
        ArrayList<Carta> cartasBarajeadas = new ArrayList<>();
        while (!lista_cartas.isEmpty()) {
            int elegirCarta = rand.nextInt(lista_cartas.size());
            Carta agregar = lista_cartas.get(elegirCarta);
            cartasBarajeadas.add(agregar);
            lista_cartas.remove(elegirCarta);
        }
        lista_cartas = cartasBarajeadas;
    }

    public void Cortar(int posicion) {
        ArrayList<Carta> cartas_cambiar = new ArrayList<>();

        if (posicion < 0 || posicion >= lista_cartas.size()) {
            System.out.println("Posicion invalida");
            return;
        }
        if (posicion == 0) {
            System.out.println("La baraja ya esta cortadayada");
            return;
        }

        for (int i = 0; i < posicion; i++) {
            cartas_cambiar.add(lista_cartas.get(0));
            lista_cartas.remove(0);
        }

        lista_cartas.addAll(cartas_cambiar);
    }

    public Carta Robar() {
        if (lista_cartas.isEmpty()) {
            return null;
        }
        Carta devolver = lista_cartas.get(0);
        lista_cartas.remove(0);
        return devolver;
    }

    public void OrdenarPorNumero(){

        if(!lista_cartas.isEmpty()){
            for(int i = 0 ; i < lista_cartas.size() -1 ; i++ ){
                for(int j = 0 ; j < lista_cartas.size() -i  -1  ; j++){
                        if (lista_cartas.get(j).getNumero() > lista_cartas.get(j+1).getNumero()){
                                Carta temp = lista_cartas.get(j);
                                lista_cartas.set(j,lista_cartas.get(j+1));
                                lista_cartas.set(j+1,temp);
                        }
                }
            }

        }


    
    }

    public void OrdenarPorPalo(){

        if(!lista_cartas.isEmpty()){
            for(int i = 0 ; i < lista_cartas.size() -1 ; i++ ){
                for(int j = 0 ; j < lista_cartas.size() -i  -1  ; j++){
                        if (lista_cartas.get(j).getNumero() > lista_cartas.get(j+1).getNumero()){
                                Carta temp = lista_cartas.get(j);
                                lista_cartas.set(j,lista_cartas.get(j+1));
                                lista_cartas.set(j+1,temp);
                        }
                }
            }

        }    
    }
     public void barajarCOnservative(){
         if(lista_cartas.size() < 10 ){
                System.out.println("Minimo 10 cartas necesarias");
                return;
         }
         // gauradar las utlimas 5 cartas 

         ArrayList <Carta> ultimas5 = new ArrayList<>();
         for(int i = lista_cartas.size()  - 5 ; i < lista_cartas.size() ; i++ ){
                ultimas5.add(lista_cartas.get(i));
         }

         // eliminar ultimas 5  de la lista principal

         for(int i = 0 ; i < 5 ; i++ ){
                lista_cartas.remove(lista_cartas.size() - 1 );
         }

         //Barajar las que quedan (algorimo simple)
         Random rd = new Random();
         for(int i = lista_cartas.size() - 1 ; i > 0 ; i-- ){
                int idx = rd.nextInt(i +1);
                Carta temp= lista_cartas.get(i);
                lista_cartas.set(i,lista_cartas.get(idx));
                lista_cartas.set(idx , temp );
         }

         // añadir las ultimas 5 al final 
         lista_cartas.addAll(ultimas5);
    }


    public void InsertaCartaFinal(int id_carta) {
        lista_cartas.add(new Carta(id_carta));
    }

    public void InsertaCartaPrincipio(int id_carta) {
        lista_cartas.add(0, new Carta(id_carta));
    }

    public void InsertaCartaFinal(Carta c) {
        lista_cartas.add(c);
    }

    public void InsertaCartaPrincipio(Carta c) {
        lista_cartas.add(0, c);
    }

    public int NumeroCartas() {
        return lista_cartas.size();
    }

    public boolean Vacia() {
        return lista_cartas.isEmpty();
    }
}
