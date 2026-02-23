package MAINSKYFYTAS;

public class Entrega {

    private Dron dron ;
    private Pedido pedido;
    private double coste_envio ;


    public Entrega(Dron dron ,  Pedido ped ){
        this.dron = dron ;
        this.pedido  = ped ; 
    }

    public double calcularTarifa(){

        return this.coste_envio = 1.20 + 0.50 * pedido.getDistanciaKm() ;
    }

    public String toString(){

        return "EL Dron es " + dron.toString() + " El plato que lleva es " + pedido.getnombreplato() + " El precio final es " + calcularTarifa();
    }

    
    
}
