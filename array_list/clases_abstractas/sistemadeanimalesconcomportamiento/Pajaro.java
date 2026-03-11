package sistemadeanimalesconcomportamiento;

public class Pajaro extends Animal {
    
    private boolean puedeVolar;

    public Pajaro(String nombre, int edad, boolean puedeVolar) {
        super(nombre, edad);
        this.puedeVolar = puedeVolar;
    }

    @Override
    public void hacerSonido() {
        System.out.println("Pío pío");
    }

    @Override
    public void moverse() {
        if (puedeVolar) {
            System.out.println("Vuela");
        } else {
            System.out.println("Anda");
        }
    }
}
