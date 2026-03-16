import java.time.LocalDate;

public class Main {
    public static void main(String[] args) {
        ClinicaVeterinaria clinica = new ClinicaVeterinaria();

        System.out.println("=== CREANDO ANIMALES ===");
        
        Perro perro1 = new Perro("Firulais", "PastorAleman", "2020-05-10", 25.5, "CHIP001");
        System.out.println("Perro creado: " + perro1);

        Gato gato1 = new Gato("Michi", "Persa", "2021-03-15", 4.5, "CHIP002");
        System.out.println("Gato creado: " + gato1);

        Pajaro pajaro1 = new Pajaro("Piolin", "Canario", "2022-01-20", 0.3, true);
        System.out.println("Pajaro creado: " + pajaro1);

        Reptil reptil1 = new Reptil("Lagarto", "Iguana", "2019-08-05", 3.0, false);
        System.out.println("Reptil creado: " + reptil1);

        Pajaro pajaro2 = new Pajaro("Loro", "Periquito", "2018-11-30", 0.5, false);
        System.out.println("Pajaro2 creado: " + pajaro2);

        System.out.println("\n=== INSERTANDO ANIMALES EN LA CLINICA ===");
        clinica.insertaAnimal(perro1);
        clinica.insertaAnimal(gato1);
        clinica.insertaAnimal(pajaro1);
        clinica.insertaAnimal(reptil1);
        clinica.insertaAnimal(pajaro2);
        System.out.println("Animales insertados correctamente");

        System.out.println("\n=== BUSCANDO ANIMALES POR NOMBRE ===");
        Animal animalBuscado = clinica.buscaAnimal("Firulais");
        if (animalBuscado != null) {
            System.out.println("Animal encontrado: " + animalBuscado);
        } else {
            System.out.println("Animal no encontrado");
        }

        Animal animalNoExiste = clinica.buscaAnimal("Pepito");
        if (animalNoExiste != null) {
            System.out.println("Animal encontrado: " + animalNoExiste);
        } else {
            System.out.println("Animal no encontrado (pepito)");
        }

        System.out.println("\n=== MODIFICANDO COMENTARIOS ===");
        boolean modificado = clinica.modificaCOmentarioAnimal("Firulais", "Paciente tranquilo, necesita paseos diarios");
        System.out.println("Comentario modificado (Firulais): " + modificado);

        boolean modificado2 = clinica.modificaCOmentarioAnimal("Michi", "Gato muy nervioso");
        System.out.println("Comentario modificado (Michi): " + modificado2);

        boolean modificado3 = clinica.modificaCOmentarioAnimal("NoExiste", "Comentario");
        System.out.println("Comentario modificado (NoExiste): " + modificado3);

        System.out.println("\n=== VERIFICANDO ANIMALES DESPUES DE MODIFICACIONES ===");
        System.out.println("Firulais: " + clinica.buscaAnimal("Firulais"));
        System.out.println("Michi: " + clinica.buscaAnimal("Michi"));

        System.out.println("\n=== PRUEBA DE VALIDACION DE ESPECIE ===");
        Perro perroInvalido = new Perro("Rex", "RazaInvalida", "2021-01-01", 20.0, "CHIP999");
        System.out.println("Perro con raza invalida: " + perroInvalido);

        System.out.println("\n=== FIN DE PRUEBAS ===");
    }
}
