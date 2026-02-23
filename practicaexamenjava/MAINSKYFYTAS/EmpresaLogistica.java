package MAINSKYFYTAS;

public class EmpresaLogistica {

    private Dron[] drones ;
    private Entrega[] entregas;
    private int contador_drones;
    private int contador_entregas;


    public EmpresaLogistica(){
        this.drones = new Dron[15];
        this.entregas = new Entrega[30];
        this.contador_drones = 0 ;
        this.contador_entregas = 0 ; 
    }


    public boolean registrarDron(Dron d ){

        if(contador_drones < drones.length ){
             drones[contador_drones++ ] = d ;
             return true ; 
        }

        return false ; 
    }
    
    public boolean enviarPedido(Pedido d ){

        for(int i= 0 ; i < drones.length ; i++ ){
                if(drones[i] != null && !drones[i].getenServicio() && drones[i].getBateria() >= 20 ){
                       drones[i].setenServicio(true);
                       drones[i].setUtilizardron(10);
                       return true ; 
                }
        }

        return false ; 
    }


    public void mostrarflota(){

        for(int i = 0 ; i < drones.length  ; i++ ){

            if(drones[i] != null && drones[i].getenServicio() ){
                System.out.println(drones[i].toString());
            }
        }
    }

    public static void main(String[] args ){

        Dron d1 = new Dron("1234", "nokia");
        Dron d2 = new Dron("12345", "sansung");
        Dron d3 = new Dron("12345" , "motorola");

        Pedido p1 = new Pedido(1, "pique", 12, 2);
        Pedido p2 = new Pedido(2, "charque", 15, 3);

        Entrega e1 = new Entrega(d1, p1);
        Entrega e2 = new Entrega(d2, p2);

        EmpresaLogistica empresa1 = new EmpresaLogistica() ;

        empresa1.registrarDron(d1);

        empresa1.mostrarflota();






    }


}
