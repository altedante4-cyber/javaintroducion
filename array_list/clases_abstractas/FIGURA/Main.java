package FIGURA;
public class Main {
    public static void main(String[] args) {
        Figura f1 = new Circulo("Rojo", 5);
        Figura f2 = new Rectangulo("Azul", 4, 3);

        f1.mostrarInfo();
        System.out.println();
        f2.mostrarInfo();
    }
}
