package pruebas;

public class Banco {

    private Cuenta [] micuenta ;
    private int contadorcuentas; 


    //creamos el contstructor

    public Banco(int tamano ){
        this.micuenta = new Cuenta[tamano];
        this.contadorcuentas = 0 ; 
    }


    // metdo seter por que modificamos el estado del array para anadir una cuenta

    public void setanadircuenta(Cuenta nuevacuenta){
        
        if(contadorcuentas < micuenta.length){
            micuenta[contadorcuentas] = nuevacuenta;
            contadorcuentas ++;
            System.out.println("Cuenta anadida Espacio total" + micuenta.length);
        }else{
            System.out.println("Erro: el banco esta lleno , capacidad maxima ");
        }
    }
 
    // metodo seter para ingresar dinero en dichas cuentas bancarias

    public boolean setingresardinero(String titular  ){
                boolean encontrado = false;                 
        for(int i = 0 ; i < micuenta.length ; i++ ){
                 if(micuenta[i].damecuenta().equals(titular)){
                    encontrado = true; 
                    break;
                 }
                 
            }      

            if(!encontrado){
                return false ; 
            }

            return true;

    }

    // hacemos un boolean para retirar dinero si el dinero no existe devolvemos false 

    
    public boolean setretirdinero(String titular  ){
                boolean encontrado = false;                 
        for(int i = 0 ; i < micuenta.length ; i++ ){
                 if(micuenta[i].damecuenta().equals(titular)){
                    encontrado = true; 
                    break;
                 }
                 
            }      

            if(!encontrado){
                return false ; 
            }

            return true;

    }

    public String toString(){
        String mostrarcuentas = "";
        for (int i =0 ; i < contadorcuentas ; i++ ){
            
             mostrarcuentas += micuenta[i] + " ";
        }
        return mostrarcuentas;
    }



    
}
