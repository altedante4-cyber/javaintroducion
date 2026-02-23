import java.util.Random;
import java.util.Scanner;

public class Persona {
    
    // Constante para el valor por defecto
    private final char SEXO_DEF = 'H';

    private String nombre, DNI;   
    private int edad; 
    private double altura, peso; 
    private char sexo; 

    // 1. Constructor por defecto
    public Persona() {
        this.nombre = "";
        this.edad = 0;
        this.altura = 0;
        this.peso = 0; 
        this.sexo = SEXO_DEF; 
        this.DNI = generaDNI(); // Invocado al construir
    }

    // 2. Constructor con nombre, edad y sexo
    public Persona(String nombre, int edad, char sexo) {
        this(); // Llama al anterior para DNI y valores por defecto
        this.nombre = nombre;
        this.edad = edad;
        comprobarSexo(sexo); // Validamos el sexo recibido
    }

    // 3. Constructor completo
    public Persona(String nombre, String DNI, int edad, char sexo, double altura, double peso) {
        this.nombre = nombre;
        this.DNI = DNI;
        this.edad = edad;
        this.peso = peso;
        this.altura = altura;
        comprobarSexo(sexo);
    }

    public int calcularIMC() {
        // Evitar división por cero si la altura es 0
        if (this.altura == 0) return -1; 
        
        double imc = this.peso / Math.pow(this.altura, 2);
        if (imc < 20) return -1;
        else if (imc >= 20 && imc <= 25) return 0;
        else return 1;
    }

    public boolean esMayorDeEdad() {
        return this.edad >= 18;
    }

    // PRIVADO: No visible al exterior
    private void comprobarSexo(char sexo) {
        if (sexo == 'H' || sexo == 'M') {
            this.sexo = sexo;
        } else {
            this.sexo = SEXO_DEF;
        }
    }

    // PRIVADO: Lógica real de DNI
    private String generaDNI() {
        Random rand = new Random();
        int num = rand.nextInt(90000000) + 10000000; // 8 cifras
        char letras[] = {'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E'};
        return String.valueOf(num) + letras[num % 23];
    }

    @Override
    public String toString() {
        return "Nombre: " + nombre + " | Sexo: " + sexo + " | Edad: " + edad + " | DNI: " + DNI + " | Altura: " + altura + " | Peso: " + peso;
    }

    // Setters y Getters (Omitidos aquí por brevedad, los tuyos estaban bien)

    



    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        String nombre = sc.nextLine();
        int edad = sc.nextInt();
        sc.nextLine() ;

        char sexo = sc.nextLine().charAt(0);
        double peso = sc.nextDouble();
        double altura = sc.nextDouble();

        Persona p1 = new Persona(nombre,"afljkdafsfa",edad, sexo,peso,altura );
Persona p2 = new Persona(nombre, edad, sexo);
Persona p3 = new Persona();
    p3.setnombre("Juan");
    p3.setedad(25);


    int resultado = p1.calcularIMC();

switch (resultado) {
    case -1 :
        System.out.println(p1.getNombre() + " está por debajo de su peso ideal.");
        break;
    case 0 :
        System.out.println(p1.getNombre() + " está en su peso ideal.");
        break;
    case 1 :
        System.out.println(p1.getNombre() + " tiene sobrepeso.");
        break;
}




    }
}