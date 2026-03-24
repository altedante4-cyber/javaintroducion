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
