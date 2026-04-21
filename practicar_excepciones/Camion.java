public class Camion{
	private String placa;
	private double peso;
	private double porcentajeMaleza ;
	public Camion(String placa , double peso , double porcentajeMaleza){
		this.placa = placa;
		this.peso = peso;
		this.porcentajeMaleza = porcentajeMaleza;
	}
	public void validarPeso() throws PesoInvalidoException {
		if(peso < 1 || peso > 25) {
		 	throw new PesoInvalidoException("Peso Invalido");
		}

	}

	public void validarMaleza() throws MalezaExcesivaException {
		if ( porcentajeMaleza > 30 ) {
		   throw new MalezaExcesivaException ("malesa excesiva");
		}

	}

	public void registrar() {
		try{
			validarPeso();
			validarMaleza();
			System.out.println("Camion registrado exitosamente");

		}catch(Exception e ){

			System.out.println(e.getMessage() );
		}
	}

}
