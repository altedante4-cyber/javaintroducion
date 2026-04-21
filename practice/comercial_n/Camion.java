public class Camion{
	private String tipo_grano;
	private double cantidad_toneladas;
	private double porcentajeMaleza;
	private double precio ;
	public Camion(String tipo_grano , double cantidad_toneladas , double porcentajeMaleza){
			this.tipo_grano = tipo_grano;
			this.cantidad_toneladas = cantidad_toneladas;
			this.porcentajeMaleza = porcentajeMaleza;
			this.precio = 0 ;
	}

	public String getTipoGrano(){ return tipo_grano;}
	public double getCatidadToneladas(){return cantidad_toneladas ;}
	public double getPorcentajeMaleza(){return porcentajeMaleza;}

	public double calcularPrecio(){ return precio += (cantidad_toneladas * 150) - porcentajeMaleza ;  }
	
	public String toString(){ return tipo_grano + cantidad_toneladas + porcentajeMaleza; }
	

}
