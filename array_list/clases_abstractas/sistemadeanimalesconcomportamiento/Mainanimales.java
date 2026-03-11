package sistemadeanimalesconcomportamiento;

public class Mainanimales {
    public static void main(String[] args) {
        Animal[] animales = new Animal[3];

        animales[0] = new Perro("Kara", 2, "Pitbull", 10);
        animales[1] = new Gato("Mishi", 1, "Verde");
        animales[2] = new Pajaro("Piolín", 3, true);

        // Polimorfismo: cada animal usa su propia implementación
        for (Animal a : animales) {
            a.mostrarInfo();
            a.hacerSonido();
            a.moverse();
            System.out.println();
        }

        // Ejemplo de uso correcto de instanceof (para datos específicos)
        for (Animal a : animales) {
            if (a instanceof Perro) {
                Perro p = (Perro) a;
                System.out.println("Raza: " + p.getClass().getSimpleName());
            }
        }
    }
}
