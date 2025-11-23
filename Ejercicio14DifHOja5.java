package und4;



// hacer un pormgamram qeu tenga una fucnion que muestre por pantall 
// la tabla de multiplicar de un numero pasado por parametro 

// hacer u porgrama que tenga dentrro de na funcion muetre por pantalll // la tabla de multplar de n numero pasado por parametro 

public class Ejercicio14DifHOja5 {

	public static void main(String[] args) {
		
		muestraTablaMultilicar(5);
		
		
		
	}
	
	public static void muestraTablaMultilicar(int num )
	{
		
		for (int i = 0 ; i <= 10 ; i++ )
		{
			 System.out.println(num + "x" + i + "== " + (num * i ));
		}
	}

}
