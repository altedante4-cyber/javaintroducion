package matriz;

public class EjercicioB {
    
    public static void main(String[] args ){

        int [][] n = new int[5][5];


        for(int i = 0 ;  i < n.length ; i++ ){

            for(int j = 0 ; j < n[i].length  ; j++ ){

                    System.out.print(n[i][j] = i * j );
            }
            System.out.println();
        }
    }
}
