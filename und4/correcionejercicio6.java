package und4;

import java.util.Scanner;

public class correcionejercicio6 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		final int TAM = 10;
		int[] num = new int[TAM];

		int suma = 0, resta = 0, mult = 1;

		double div = 1;
		Scanner entrada = new Scanner(System.in);

		// rellenamos el array

		for (int i = 0; i < TAM; i++) {

			do {

				System.out.println("introduce valor ");

				num[i] = entrada.nextInt();

			} while (num[i] == 0);

		}

		// incializamos las variables al primer valor del aarrays

		// posicion del array
		//
		div = num[0];
		suma = num[0];
		resta = num[0];
		mult = num[0];

		for (int i = 1; i < TAM; i++) {

			suma = suma + num[i];
			resta = resta - num[i];
			mult = mult * num[i];
			div = div / num[i];
		}
		
 
		System.out.println("esto es la suma " +  suma );

		System.out.println("esto es la resta" +  resta );

		System.out.println("esto es la mult " +  mult );

		System.out.println("esto es la division " +  div );

	}

}
