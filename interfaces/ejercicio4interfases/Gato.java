package ejercicio4interfases;

public class Gato extends Animal implements Hablador {

    @Override
    public void saludar(){
        saludar();
        System.out.println("ESTO ES UN GATO");
    }
    
}
