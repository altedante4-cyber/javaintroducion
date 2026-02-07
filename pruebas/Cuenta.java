package pruebas;
public class Cuenta {

    // enpaquetamos los atributos
    private String titular;
    private double cantidad;

    // construimos la clase
    public Cuenta(String titular , double cantidad ){
        
        this.titular = titular;
        this.cantidad = cantidad ; 
    }
    // pero como dice el enunciado se le puede pasar como parametro solo el titular

    public Cuenta(String titular ){
        this.titular=titular;
        this.cantidad = 0 ; 
    }


    // creamos los metodos getter y setter

    public void ingresarcantidad(double cantidad){
        if ( cantidad > 0 ){
            this.cantidad +=  cantidad;
        }
    }

    // retirar dinero

    public void retirardinero(double cantidad){
       
        this.cantidad -= cantidad;
        
        if(this.cantidad < 0 ){
            this.cantidad = 0 ;
        } 

    }

    // mostramos el resultado con el tostring

    public String toString(){

        return  "El usuario " + titular + "tiene sueldo total de " + cantidad;
    }

    // dame cuenta 

    public String damecuenta(){

         return titular ;
    }










    

    
}
