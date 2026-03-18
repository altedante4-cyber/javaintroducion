public class main {

    public static void main(String[] args ){
         
          Persona p1 = new Persona("miki", 12);
          Persona p2 = new Persona("miki", 12);

          if(p1.equals(p2)){
             System.out.println("son iguales");
          }else{
            System.out.println("son distintos ");
          }
    }
}
