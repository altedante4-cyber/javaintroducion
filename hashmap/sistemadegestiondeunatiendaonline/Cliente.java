package sistemadegestiondeunatiendaonline;

public class Cliente {
    private int id ;
    private String nombre;
    private String email ;

    public Cliente(int id , String nombre , String email ){

         this.id = id ;
         this.nombre = nombre ;
         this.email = nombre ; 
    }

    public String toString(){
         
        return " el id  " + id + " el nombre es  " + nombre + " el email es  " + email ; 
    }

    

}
