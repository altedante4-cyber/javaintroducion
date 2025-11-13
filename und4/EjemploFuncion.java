package und4;

public class EjemploFuncion {

	public static void main(String[] args) { // aqui va todo lo que  se ve 
		// TODO Auto-generated method stub

		int resultado = suma(2,3);
		
		System.out.println(resultado);
		
		
	}

	
	//paso 1. definimos la ufnion suma 
	
	// cabecera 
	
	public static int suma(int a , int b ) {
		
		// cuerpo 
		
		int rsdo  = a +b;
		
		return rsdo ; 
	}
	
	// no aparece nada en la terminal por que   todo lo que aparece tiene que esta en main 
	
	
}
