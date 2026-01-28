package javaintroducion;
public class Persona {
    private String dni;
    private Cuenta[] cuentas; // Atributo en minúscula por convención
    private int numCuentaAsociadas; 

    /*
     * +persona(dni) 
+agregarcuenta(cuenta):boolean
+enmorosa():boolean
+tostring[]:string
+dameCuenta(numcuenta):cuenta


     * */

    
    public Persona(String dni) {
        this.dni = dni;
        cuentas = new Cuenta[3];
        numCuentaAsociadas = 0 ;
        
    }
    
    public boolean agregarcuenta(Cuenta c ) {
    	 /// devuelve un booleanno<<<<<<<<>>>>>>>> si se agrego correctamente 
          
    	if(numCuentaAsociadas >= 3 ) {
    		return false ; 
    	    		
    	}
    	
    	// hay espacio 
		// 
		cuentas[numCuentaAsociadas] = c;
		numCuentaAsociadas ++ ; 
		return true ; 
		
    
        
          
    }
    
    
    public String toString() {
    	String cad = "dni"+dni+"/n"+ "Cuentas " ;
    	for (int i = 0 ; i < numCuentaAsociadas ; i++ ) {
    		 
    		cad += cuentas[i].toString();
    	}
    	
    	return cad ; 
    	
    }
    
    
   	
		
}