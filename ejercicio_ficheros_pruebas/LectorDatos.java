import java.util.Scanner;
public class LectorDatos{

	public static void main(String [] args){
		Scanner sc = new Scanner(System.in);
		try{
			System.out.println("Ingrese el nombre archivo");
			String name = sc.nextLine();
			leer(name);
		}catch(ArchivoException e ){
			System.out.println(e);

		}
	}

	public static void leer(String archivo) throws ArchivoException {
		if(archivo == null){
			throw new ArchivoException ("El archivo no existe");
		}else if ( archivo.isEmpty()){
			throw new ArchivoException ("El archivo esta vacio");
		}else{

			throw new ArchivoException  ("Error de lectura");
		}

	}
	
}
