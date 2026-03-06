package EJERCICOI2_8;

public class Bebida extends ItemMenu {

    private String tamanao ;
    private boolean tieneAlcohol ;


    public Bebida(String nombre , String descripcion , double precioBase , String tamano ){
        super(nombre, descripcion, precioBase);
        this.tamanao = tamano ; 
    }

    @Override
    public double calcularPrecioFinal(){
        if(tamanao.equalsIgnoreCase("Grande"))return super.calcularPrecioFinal() + 1.5 ; 
        return super.calcularPrecioFinal() ; 
    }

    

}
