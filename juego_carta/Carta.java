public class Carta {

    private int numero;
    private int palo;

    private static String[] nombreNumero = {"as", "dos", "tres", "cuatro", "cinco", "seis", "siete", "sota", "caballo", "rey"};
    private static String[] nombrePalos = {"oros", "copas", "espadas", "bastos"};

    public Carta(int numero, int palo) {
        setNumero(numero);
        setPalo(palo);
    }

    public Carta(int id) {
        if (id >= 1 && id <= 10) {
            this.numero = id;
            this.palo = 0;
        } else if (id >= 11 && id <= 20) {
            this.numero = id - 10;
            this.palo = 1;
        } else if (id >= 21 && id <= 30) {
            this.numero = id - 20;
            this.palo = 2;
        } else if (id >= 31 && id <= 40) {
            this.numero = id - 30;
            this.palo = 3;
        }
    }
    public void setNumero(int numero ){
         if (numero < 0 || numero > 10  ) this.numero = 0 ;
         this.numero = numero;
    }
    public void setPalo(int palo){
        if(palo < 0 || palo > 3 ) this.palo = 0 ;
         this.palo = palo ; 
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
    public String toString(){
        return "Numero " + numero + "Palo " + palo ; 
    }
}
