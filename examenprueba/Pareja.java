package examenprueba;

public class Pareja {

	private Persona persona1;
	private Persona persona2 ; 
	private Regalo regaloParaPersona1;
	private Regalo regaloParaPersona2 ; 
	
	// metodo constructo 
	
	public Pareja(Persona p1 , Persona p2 ) {
		
		 	this.persona1 = p1;
		 	this.persona2 = p2 ; 
		 	this.regaloParaPersona1 = null ;
		 	this.regaloParaPersona2 = null ;
	}
	
	
	public void setRegaloParaPersona1(Regalo regalo ) {
		 // tenemos como parametro el objeto regalo y ese regalo tiene que ser asignado  a una persona 
		
		this.persona1. = this.regaloParaPersona1.this.persona1.damenombrepersona());
		this.regaloParaPersona1.setdameelpreciodelregalo(regalo.dameprecio());
		this.regaloParaPersona1.setdameladescripciondelregalo(regalo.damedescripcion());
		  
		  
		
	
			
			
	}
	
	public void setRegaloParaPersona2(Regalo regalo) {
		 // tenemos como parametro el objeto regalo y ese regalo tiene que ser asignado  a una persona 
		
	 		this.regaloParaPersona2.setnombredelregalo(null);
	 		this.regaloParaPersona2.setdameladescripciondelregalo(null);
		 	this.regaloParaPersona2.setdameelpreciodelregalo(0);
	}
	
	public double calcularCostoTotal() {
		
		return this.regaloParaPersona1.dameprecio() ; 
	}
	
	public void mostrarDetalles() {
		
		System.out.println("El regalo de la persona1 " + this.regaloParaPersona1.damenombre() + "con el precio de " + this.regaloParaPersona1.dameprecio() + "con la descripcion" + this.regaloParaPersona1.damedescripcion());
		System.out.println("El regalo de la persona1 " + this.regaloParaPersona2.damenombre() + "con el precio de " + this.regaloParaPersona2.dameprecio() + "con la descripcion" + this.regaloParaPersona2.damedescripcion());
	}
	
}
