import java.util.Scanner ; 
public class mainprobar{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		String placa = sc.nextLine();
		double tone = sc.nextDouble();
		double porce = sc.nextDouble();
		Camion ne = new Camion(placa,tone,porce);

		try{
			ne.validarPeso();
			ne.validarMaleza();

			ne.registrar();
		}catch(Exception e) {
		System.out.println(e.getMessage());
	}

	}
}
