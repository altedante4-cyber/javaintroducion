package Intefaces;

public class Paloma extends Ave  {
    private String color , sexo  ;
    public Paloma(boolean vuela , String especie , String color , String sexo   ){
        super(vuela,especie); 
        this.color = color ;
         this.sexo = sexo ;
    }
}
