package examenprueba;

public class Regalo {
	
	private String nombre ; 
	private  double precio ;
	private String descripcion ; 
	
	
	public Regalo(String nombre , double precio , String descripcion) {
		
		this.nombre = null;
		this.precio = 0;
		this.descripcion = null; 
		
		
	}
	


	// los metodos geter
	
	public String damenombre() {
		return this.nombre ; 
	}
	public double dameprecio() {
		return this.precio; 
	}
	public String damedescripcion() {
		return this.descripcion ; 
	}
	
	// metoedo seter 
	
	public void setnombredelregalo(String nombre) {
		this.nombre = nombre ; 
	}
	public void setdameelpreciodelregalo(double precio) {
		this.precio = precio ;
	}
	public void setdameladescripciondelregalo(String descripcion) {
		this.descripcion = descripcion ; 
	}
	
	
	
	public String toString() {
		
		return "El nombre " +nombre + "con el precio" + precio + "con una descripcion" + descripcion ; 
	}
	
	
	
}
