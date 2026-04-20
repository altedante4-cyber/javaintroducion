public class Alumno{
	private String nombre;
	private int edad;
	private double calificacion;

	public Alumno(String nombre , int edad , double calificacion ){
		setNombre(nombre);
		setEdad(edad);
		setCalificacion(calificacion);
	}

	public String getNombre(){return nombre ; };
	public int getEdad(){return edad;};
	public double getCalificacion(){return calificacion;};
	public void setNombre(String name){ 
		if (name == null || name.isEmpty()){ 
			throw new IllegalArgumentException("El nombre no puede estar vacío"); 
		}
		this.nombre = name ;
	};
	public void setEdad(int y){
		if(y >= 0 && y <= 100){
		this.edad = y; 
		}
	};
	public void setCalificacion(double n){ 
		if(n >= 0 && n <= 10) { 
		this.calificacion = n; 
	}
}
	
	public String imprime(){
		return  nombre + " "+ edad + " "+ calificacion ;
	}
}
