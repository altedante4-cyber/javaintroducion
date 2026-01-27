package javaintroducion;
public class Persona {
    private String dni;
    private Cuenta[] cuentas; // Atributo en minúscula por convención

    /*
     * +persona(dni) 
+agregarcuenta(cuenta):boolean
+enmorosa():boolean
+tostring[]:string
+dameCuenta(numcuenta):cuenta


     * */

    
    public Persona(String dni, Cuenta[] cuentas) {
        this.dni = dni;
        this.cuentas = new Cuenta [3];
    }
    
    public void Persona_dni(String dni){
    	this.dni = dni ; 

    }
    
    public boolean agregarcuenta(String cuenta) {
    	 /// devuelve un booleanno<<<<<<<<>>>>>>>> si se agrego correctamente 
          
         for (int i = 0 ; i < cuentas.length ; i++ ){

              if(!cuentas.equals(null) || !cuentas.equals(' ')){
                 return true ; 
              }
         }

         return false ; 
        
          
    }
    
    public boolean esMorosa(double a) {
    	   
    	//devuelve  un booleano true si es morosa o no 
    	if ( a >= 0.0 ){
            return true ; 

        }
    	
        return false ; 
    	
    
    }
    
    public String damecuenta(String cuenta []) {
    	  
    	 
    }
   	
		
}