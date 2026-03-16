package ejercicio3conjuntospepalabrasconhashset;

import java.util.HashSet;

public class Main {
    public static void main(String[] args) {
        System.out.println("=== Prueba de Palabra ===");
        
        HashSet<String> sinonimos1 = new HashSet<>();
        sinonimos1.add("alegre");
        sinonimos1.add("contento");
        
        Palabra palabra1 = new Palabra("feliz", sinonimos1);
        System.out.println("Palabra creada: " + palabra1);
        System.out.println("Getter palabra: " + palabra1.getPalabra());
        System.out.println("Getter sinonimos: " + palabra1.getsinonimos());
        
        palabra1.setSinonimos("dichoso");
        System.out.println("Despues de agregar sinonimo: " + palabra1);
        
        System.out.println("\n=== Prueba de Diccionario ===");
        
        Diccionario diccionario = new Diccionario();
        
        HashSet<String> sinonimos2 = new HashSet<>();
        sinonimos2.add("triste");
        sinonimos2.add("melancolico");
        Palabra palabra2 = new Palabra("triste", sinonimos2);
        
        HashSet<String> sinonimos3 = new HashSet<>();
        sinonimos3.add("alegre");
        sinonimos3.add("animado");
        sinonimos3.add("feliz");
        Palabra palabra3 = new Palabra("contento", sinonimos3);
        
        boolean added1 = diccionario.AgregarPalabrasSinonimos(palabra1);
        boolean added2 = diccionario.AgregarPalabrasSinonimos(palabra2);
        boolean added3 = diccionario.AgregarPalabrasSinonimos(palabra3);
        
        System.out.println("Palabra 1 agregada: " + added1);
        System.out.println("Palabra 2 agregada: " + added2);
        System.out.println("Palabra 3 agregada: " + added3);
        
        System.out.println("\n=== Agregar sinonimo a palabra existente ===");
        boolean agregarSino = diccionario.AgregarSinonimosPalabraExistente("feliz", "satisfecho");
        System.out.println("Sinonimo agregado a 'feliz': " + agregarSino);
        System.out.println("Palabra 1 ahora: " + palabra1);
        
        boolean agregarSinoInexistente = diccionario.AgregarSinonimosPalabraExistente("inexistente", "algo");
        System.out.println("Agregar a palabra inexistente: " + agregarSinoInexistente);
        
        System.out.println("\n=== Mostrar todas las palabras y sinonimos ===");
        diccionario.mostrarPalabraysinonimos();
        
        System.out.println("\n=== Sinonimos comunes entre palabra2 y palabra3 ===");
        diccionario.encontrarSinonimosComunes(palabra2, palabra3);
        
        System.out.println("\n=== Prueba de agregar palabra duplicada ===");
        boolean duplicate = diccionario.AgregarPalabrasSinonimos(palabra1);
        System.out.println("Duplicado agregado: " + duplicate);
    }
}
