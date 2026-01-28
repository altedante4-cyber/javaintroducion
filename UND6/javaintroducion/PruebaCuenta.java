package javaintroducion;
import java.util.Scanner;

public class PruebaCuenta {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // "Base de datos" de personas (el parking de objetos)
        Persona base_per[] = new Persona[10];
        int posicion_base_datos = 0; 
        int opcion = 0;

        do {
            System.out.println("\n--- SISTEMA BANCARIO ---");
            System.out.println("1. Añadir persona");
            System.out.println("2. Buscar persona (Mostrar datos)");
            System.out.println("3. Añadir cuenta a persona");
            System.out.println("4. Realizar transferencia/ingreso");
            System.out.println("5. Salir");
            System.out.print("Elija una opción: ");
            
            opcion = sc.nextInt();
            sc.nextLine(); // Limpiar el buffer después de leer un número

            switch (opcion) {
                case 1:
                    if (posicion_base_datos < 10) {
                        System.out.print("Introduzca el DNI: ");
                        String dni = sc.nextLine();
                        // CREACIÓN DEL OBJETOS: Aquí nace la persona
                        base_per[posicion_base_datos] = new Persona(dni);
                        posicion_base_datos++;
                        System.out.println("Persona registrada correctamente.");
                    } else {
                        System.out.println("Error: Base de datos llena.");
                    }
                    break;

                case 2:
                    System.out.print("DNI de la persona a buscar: ");
                    String dniB = sc.nextLine();
                    boolean hallado = false;
                    // BÚSQUEDA: Usamos posicion_base_datos para evitar nulos
                    for (int i = 0; i < posicion_base_datos; i++) {
                        if (base_per[i].dameDni().equals(dniB)) {
                            System.out.println(base_per[i].toString());
                            hallado = true;
                            break;
                        }
                    }
                    if (!hallado) System.out.println("La persona no existe.");
                    break;

                case 3:
                    System.out.print("DNI del titular para la nueva cuenta: ");
                    String dniT = sc.nextLine();
                    Persona pTitular = null;
                    for (int i = 0; i < posicion_base_datos; i++) {
                        if (base_per[i].dameDni().equals(dniT)) {
                            pTitular = base_per[i];
                            break;
                        }
                    }
                    if (pTitular != null) {
                        System.out.print("Número de la nueva cuenta: ");
                        String nC = sc.nextLine();
                        System.out.print("Saldo inicial: ");
                        double sI = sc.nextDouble();
                        // CREACIÓN DE CUENTA: Se crea y se agrega al array de la persona
                        if (pTitular.agregarcuenta(new Cuenta(nC, sI))) {
                            System.out.println("Cuenta vinculada con éxito.");
                        } else {
                            System.out.println("Error: Ya tiene el máximo de 3 cuentas.");
                        }
                    } else {
                        System.out.println("Error: Primero debe registrar a la persona (Opción 1).");
                    }
                    break;

                case 4:
                    System.out.print("DNI del titular: ");
                    String dniP = sc.nextLine();
                    Persona pActiva = null;
                    for (int i = 0; i < posicion_base_datos; i++) {
                        if (base_per[i].dameDni().equals(dniP)) {
                            pActiva = base_per[i];
                            break;
                        }
                    }

                    if (pActiva != null) {
                        System.out.println("1. Ingreso directo / 2. Transferencia entre mis cuentas");
                        int subOpcion = sc.nextInt();
                        sc.nextLine();

                        if (subOpcion == 1) {
                            System.out.print("Número de cuenta: ");
                            String nCuenta = sc.nextLine();
                            if (pActiva.cuentavalida(nCuenta)) {
                                System.out.print("Monto a ingresar: ");
                                double monto = sc.nextDouble();
                                pActiva.obtenerCuenta(nCuenta).recibirABonons(monto);
                                System.out.println("Saldo actualizado.");
                            } else {
                                System.out.println("Cuenta no encontrada.");
                            }
                        } else if (subOpcion == 2) {
                            System.out.print("Cuenta de ORIGEN: ");
                            String cOri = sc.nextLine();
                            System.out.print("Cuenta de DESTINO: ");
                            String cDes = sc.nextLine();
                            
                            if (pActiva.cuentavalida(cOri) && pActiva.cuentavalida(cDes)) {
                                System.out.print("Monto a transferir: ");
                                double tMonto = sc.nextDouble();
                                if (pActiva.obtenerCuenta(cOri).PagarRecibo(tMonto)) {
                                    pActiva.obtenerCuenta(cDes).recibirABonons(tMonto);
                                    System.out.println("Transferencia realizada.");
                                }
                            } else {
                                System.out.println("Alguna de las cuentas no existe.");
                            }
                        }
                    } else {
                        System.out.println("Usuario no encontrado.");
                    }
                    break;

                case 5:
                    System.out.println("Cerrando aplicación...");
                    break;

                default:
                    System.out.println("Opción no válida.");
            }
        } while (opcion != 5);
        
        sc.close();
    }
}