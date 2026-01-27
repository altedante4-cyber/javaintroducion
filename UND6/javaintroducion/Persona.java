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

    
    public Persona(String dni, Cuenta[] cuentasRecibidas) {
        this.dni = dni;
        this.cuentas = cuentasRecibidas;
    }
    
    public void Persona_dni(String dni){
    	this.dni = dni ; 

    }
    
    public boolean agregarcuenta(String cuenta []) {
    	 /// devuelve un booleanno<<<<<<<<>>>>>>>> si se agrego correctamente 
    	  
    }
    
    public boolean esMorosa() {
    	   
    	//devuelve  un booleano true si es morosa o no 
    	
    	
    	
    
    }
    
    public String damecuenta(String cuenta []) {
    	  
    	 
    }
   	
		
}