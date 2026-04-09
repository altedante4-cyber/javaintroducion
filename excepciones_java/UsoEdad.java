public class UsoEdad {
    public static void validarEdad(int edad) throws Edadnoestaenrango {

            if(edad >= 0 && edad <= 100 ){
                 throw new Edadnoestaenrango("La edad no esta en rango ");
            }
        

    }
    public static void main(String [] args){

            try{
                validarEdad(-1);

            }catch(Edadnoestaenrango a){
                System.out.println(a.getMessage());
                 
            }
    }
    
}
