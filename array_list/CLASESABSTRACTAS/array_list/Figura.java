package array_list;

public abstract  class  Figura {

	
	protected String nombre ;
	
	public Figura(String nombre ) {
		
		this.nombre = nombre ;
	}
	
	
	
	  public  String   getNombre() {
		
		  return nombre ; 
		  
		  
	}
	  
	  // area de un punto  area  0  volumen  0 
	  //  area de un  pi  radicuadrado   volumen es 4 / 3 por pi por radio cubito
	  
	  
	 protected abstract double obtenerArea();
		   
	protected  abstract double obtenerAreaPunto();
	
	  protected  abstract double  obtenerVolumen();
}
