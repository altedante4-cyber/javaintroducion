package Ejercicio3;

public class Persona {

	private String nombre , apellido , DNI, estado_civil;

	public Persona(String nombre , String apellido , String DNI , String estado_civil ) {
			
			this.nombre = nombre ; 
			this.apellido = apellido ; 
			this.DNI = DNI; 
			this.estado_civil = estado_civil ; 
		
	}
	
	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getApellido() {
		return apellido;
	}

	public void setApellido(String apellido) {
		this.apellido = apellido;
	}

	public String getDNI() {
		return DNI;
	}

	public void setDNI(String dNI) {
		DNI = dNI;
	}

	public String getEstado_civil() {
		return estado_civil;
	}

	public void setEstado_civil(String estado_civil) {
		this.estado_civil = estado_civil;
	}

	@Override
	public String toString() {
		return "Persona [nombre=" + nombre + ", apellido=" + apellido + ", DNI=" + DNI + ", estado_civil="
				+ estado_civil + "]";
	}
	
	
	

}
