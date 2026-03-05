package matriz;

import java.util.Random ; 
public class ejercicio1 {

    public static void main (String[] args ){

        int [][] n = new int[5][5];

        int k = 1; 
        for (int i = 0 ; i < n.length ; i++ ){

            for (int  j = 0 ; j < n[i].length ; j ++ ){
                  
                System.out.print(n[i][j] += k) ; 

                k++; 


            }
            System.out.println();
        }
    }
    
}
