package sistemadeanimalesconcomportamiento;

public class Perro extends Animal {
    
    private String raza;
    private int velocidadCarrera;

    public Perro(String nombre, int edad, String raza, int velocidadCarrera) {
        super(nombre, edad);
        this.raza = raza;
        this.velocidadCarrera = velocidadCarrera;
    }

    @Override
    public void hacerSonido() {
        System.out.println("Guau guau");
    }

    @Override
    public void moverse() {
        System.out.println("Corre a " + velocidadCarrera + " km/h");
    }
}
