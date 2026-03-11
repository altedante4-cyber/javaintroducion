package sistemadeanimalesconcomportamiento;

public class Gato extends Animal {
    
    private String colorOjos;

    public Gato(String nombre, int edad, String colorOjos) {
        super(nombre, edad);
        this.colorOjos = colorOjos;
    }

    @Override
    public void hacerSonido() {
        System.out.println("Miau");
    }

    @Override
    public void moverse() {
        System.out.println("Salta");
    }
}
