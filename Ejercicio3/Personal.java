

public class Personal  extends Persona {

	
	private int anio_incorporacion , n_despacho , n_seccion ;

	
	public Personal(String nombre , String apellido , String DNI , String estado_civil,int anio_incorporacion , int n_despacho , int n_seccion ) {
		
		super(nombre , apellido , DNI , estado_civil  );
		this.anio_incorporacion = anio_incorporacion ;
		this.n_despacho = n_despacho;
		this.n_seccion = n_seccion ; 
		
		
	}
	public int getAnio_incorporacion() {
		return anio_incorporacion;
	}

	public void setAnio_incorporacion(int anio_incorporacion) {
		this.anio_incorporacion = anio_incorporacion;
	}

	public int getN_despacho() {
		return n_despacho;
	}

	public void setN_despacho(int n_despacho) {
		this.n_despacho = n_despacho;
	}

	public int getN_seccion() {
		return n_seccion;
	}

	public void setN_seccion(int n_seccion) {
		this.n_seccion = n_seccion;
	}

	@Override
	public String toString() {
		return "Personal [anio_incorporacion=" + anio_incorporacion + ", n_despacho=" + n_despacho + ", n_seccion="
				+ n_seccion + "]";
	} 

	

}
