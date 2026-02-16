package examenprueba;

public class Persona {

	
	private String dni ; 
	private String nombre ;
	
	
	// creasmo el metod construcftor
	
	public Persona(String dni , String nombre ) {
		
		this.dni = dni ;
		this.nombre = nombre ; 
	}

	
	
	

	
	// metodos de acceso de lectrura es decir que son geter
	
	
	
	public String damedni() {
		return this.dni;
	}
	
	public String damenombrepersona() {
			return this.nombre ;
	}
	
	
	public String toString() {
		
		 return "El nombre de la persona " + nombre + "con el DNI" + dni ; 
	}
}
