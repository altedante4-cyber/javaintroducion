package UND7;

public class Coche extends  Vehiculo  {

	private int cv;

	//constructor
	
	public Coche(boolean tieneMotor , int numRuedas , String color , String matricula , int cv) {
		
		
		// construimos un vehiuclo
		// con super llamamos al consturctor de la clase padre
		
		super(true,4,color , matricula ); // solo los atributos del padre 
		this.cv = cv ; 
		
		
	}
	
	
	public int getCV() {
		return cv;
	}
	
	public void setCV(int  cv ) {
		this.cv = cv ; 
	}
	
	public String toString() {
		
		return super.toString() + "CV :" + cv ; 
	}
	
	
	
	
}
