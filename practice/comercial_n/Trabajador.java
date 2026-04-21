import java.io.FileWriter;
import java.io.IOException;
public class Trabajador{

	private String nombre;
	private double toneladasProcesadas;
	private double quintales;
	private double total;
	public Trabajador(String nombre , double toneladasProcesadas,double quintales){
			this.nombre = nombre;
			this.toneladasProcesadas=toneladasProcesadas;
			this.quintales=quintales;
			this.total = 0;
	}

	public double calcularPago(){
		return total += toneladasProcesadas * 100 + quintales * 2 ;
	}	
	public double getTotal(){ return total ; }
	public double getQuintales(){return quintales;}
	public String getNombre(){ return nombre;}
	public double getToneladas(){ return toneladasProcesadas;}

	public String toString(){ return nombre + "," + toneladasProcesadas ;}
	public void escribir_archivo() throws Exception {
		FileWriter escribir = new FileWriter("jornada.txt");
		try{
			escribir.write(this.toString());
		}catch(IOException e){

		System.out.println("No se pudo escribir correctamente en el archivo");
	}
	}


}
