package matriz;

public class EjercicioC {
    public static void main(String[] args ){

     int [][] n = new int[5][5];

        for (int i = 0 ; i < n.length ; i++ ){

            for (int  j = 0 ; j < n[i].length ; j ++ ){
                  
                

            n[i][j] = i+ j;
                

            }
            System.out.println();
        }
        
        for (int i = 0 ; i < n.length ; i++ ){

            for (int  j = 0 ; j < n[i].length ; j ++ ){
                  
                    
                if(n[i][j] == 4 || n[i][j] % 2 == 0 ){
                    System.out.print("1");

                }else{
                    System.out.print("0");

                }             

            }
            System.out.println();
        }
        
    
    

    }
}
