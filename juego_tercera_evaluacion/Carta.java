public class Carta {

    private int numeroCarta;
    private int  palOCartas ;
    private int id ; 

    public Carta(int numeroCartas, int palo){
         this.numeroCarta = numeroCartas;
         this.palOCartas = palo ; 
    }

    public Carta(int id ){

        this.id = id ;
    }


    public int Numero(){
         return numeroCarta ; 
    }

    public int Palo(){
        return palOCartas;
    }

    public String NombreNumero(){
        String numerocarta_str [] = {"as","dos","tres","cuatro","cinco","seis","siete","sota","caballo","rey" };
        return String.valueOf(numeroCarta) +"="+ numerocarta_str[numeroCarta -1 ] ; // aqui obtenes el valor string
        }

    public String NombreCarta(){
      // es el numero + palo 
      String palocarta_str [] = {"oros","copas","espada","bastos"};
      String numero_carta_str [] = NombreNumero().split("=") ;
      return palocarta_str[palOCartas] + "de" + numero_carta_str[1];
    }
    public int ValorTute(){
         int valor [] = {11,0,10,0,0,0,0,2,3,4};
         String obtener_nombre [] = NombreNumero().split("=") ;
         // convertimos a numeor 
         int numero = Integer.parseInt(obtener_nombre[0]);
         return valor[numero-1];
    }
    
     public int ValorMus(){
         int valor [] = {1,1,10,0,0,0,0,10,10,10};
         return valor[Numero() - 1 ];
    }
    
      
    public double Valor7ymedia(){
         double  valor [] = {1,2,3,4,5,6,7,0.5,0.5,0.5};
         return valor[Numero() - 1 ];
        }


    }

    

