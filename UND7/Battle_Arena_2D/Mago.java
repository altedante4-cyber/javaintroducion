package Battle_Arena_2D;

public class Mago extends Personaje {
    

    public Mago(String nombre , int vida , int magia){

        super(nombre, vida, magia);

    }


    @Override

    public int atacar(){

        if( getmagia() >=5 ){ // le enunciado decia la menos 5
            setmagia(); 
            return getatacar() * 3 ; 
        }
        System.out.println("Sin magia ");
        return 0 ; // si no tiene magia dano 0 
    }


    public String toString(){

        return super.toString() ; 
    }

}

