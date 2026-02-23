package MAINSKYFYTAS;

public class Pedido {
    private int numeroPedido;
    private String nombrePlatos;
    private double PesoGramos;
    private double distanciaKM;


    public Pedido(int numeroPedido , String nombrePlatos , double PesoGramos , double distanciaKm ){
        this.numeroPedido = numeroPedido;
        this.nombrePlatos = nombrePlatos;
        this.PesoGramos = PesoGramos ;
        this.distanciaKM = distanciaKm ; 
    }


    public double  getDistanciaKm(){

        return distanciaKM ;

    }


    public String getnombreplato(){
        return nombrePlatos ; 
    }


    

}
