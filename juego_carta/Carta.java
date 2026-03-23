public class Carta {

    private int numero;
    private int palo;

    private static String[] nombreNumero = {"as", "dos", "tres", "cuatro", "cinco", "seis", "siete", "sota", "caballo", "rey"};
    private static String[] nombrePalos = {"oros", "copas", "espadas", "bastos"};

    public Carta(int numero, int palo) {
        this.numero = numero;
        this.palo = palo;
    }

    public Carta(int id) {
        this.numero = ((id - 1) % 10) + 1;
        this.palo = (id - 1) / 10;
    }

    public int getNumero() {
        return numero;
    }

    public int getPalo() {
        return palo;
    }

    public String NombreNumero() {
        return nombreNumero[numero - 1];
    }

    public String NombrePalo() {
        return nombrePalos[palo];
    }

    public String NombreCarta() {
        return NombreNumero() + " de " + NombrePalo();
    }

    public int ValorTute() {
        int[] numeroTute = {11, 2, 10, 4, 5, 6, 7, 2, 3, 4};
        return numeroTute[numero - 1];
    }

    public int ValorMus() {
        int[] numeroMus = {1, 1, 10, 4, 5, 6, 7, 10, 10, 10};
        return numeroMus[numero - 1];
    }

    public double Valor7ymedia() {
        double[] numeroMedia = {1, 2, 3, 4, 5, 6, 7, 0.5, 0.5, 0.5};
        return numeroMedia[numero - 1];
    }
}
