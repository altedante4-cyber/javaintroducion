package UND7;

public class Vehiculo {

    private boolean tieneMOtor;
    private int numRuedas;
    private String color , matricula ;
    
    
    
    public Vehiculo(boolean tieneMotor , int numRuedas , String color , String matricula ) {
    		
    	this.tieneMOtor = tieneMotor;
    	this.numRuedas = numRuedas;
    	this.color = color;
    	this.matricula = matricula ; 
    }
    
    
	public boolean isTieneMOtor() {
		return tieneMOtor;
	}
	public void setTieneMOtor(boolean tieneMOtor) {
		this.tieneMOtor = tieneMOtor;
	}
	public int getNumRuedas() {
		return numRuedas;
	}
	public void setNumRuedas(int numRuedas) {
		this.numRuedas = numRuedas;
	}
	public String getColor() {
		return color;
	}
	public void setColor(String color) {
		this.color = color;
	}
	public String getMatricula() {
		return matricula;
	}
	public void setMatricula(String matricula) {
		this.matricula = matricula;
	} 
	
	


    
    
}
