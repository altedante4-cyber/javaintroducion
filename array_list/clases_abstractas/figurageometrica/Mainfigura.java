package figurageometrica;

public class Mainfigura {
    public static void main(String[] args) {
        // Mejorado: usando array para demostrar polimorfismo
        Poligono[] figuras = new Poligono[3];
        
        figuras[0] = new Triangulo("verde", 2, 2, 5, 2, 3);
        figuras[1] = new Cuadrado("rojo", 5);
        figuras[2] = new Circulo("gris", 3);

        // Polimorfismo: cada objeto usa su propia implementación
        for (Poligono p : figuras) {
            p.mostrarInfo();
        }
    }
}
