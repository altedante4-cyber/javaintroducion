package MAINSKYFYTAS;

public class Dron {
    private String idDron;
    private String modelo ;
    private int bateria;
    private boolean enServicio ;

    public Dron(String idDron , String modelo ){
        this.idDron = idDron;
        this.modelo = modelo;
        setbateria(100);
        this.enServicio = false ;
    }

    public void setenServicio(boolean enservicio ){

         this.enServicio = enservicio ;
    }

    public int getBateria(){
        return bateria ;
    }

    public void setbateria(int bateria){
        if(bateria >= 0 && bateria <= 100 ){
            this.bateria = bateria ;
        }

        this.bateria = 100; 
    }


    public boolean getenServicio(){
        return enServicio;
    }

    public void setUtilizardron(int bateria ){

         this.bateria -= bateria ; 
    }

    public String toString(){
        return "ID " + idDron + " el modelo  es " + modelo + " se encuentra en " + enServicio ;
    }
    
}
