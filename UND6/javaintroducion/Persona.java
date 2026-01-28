package javaintroducion;

public class Persona {
    private String dni;
    private Cuenta[] cuentas;
    private int numCuentaAsociadas;

    public Persona(String dni) {
        this.dni = dni;
        this.cuentas = new Cuenta[3]; 
        this.numCuentaAsociadas = 0;
    }

    public boolean agregarcuenta(Cuenta c) {
        if (numCuentaAsociadas < 3) {
            cuentas[numCuentaAsociadas] = c;
            numCuentaAsociadas++;
            return true;
        }
        return false;
    }

    /**
     * CORRECCIÓN: Verifica si el número de cuenta pertenece a esta persona.
     * Accedemos a cuentas[i].dameCuenta() para comparar el String.
     */
    public boolean cuentavalida(String numeroABuscar) {
        for (int i = 0; i < numCuentaAsociadas; i++) {
            // Comparamos el String del número de cuenta del objeto con el ingresado
            if (cuentas[i].dameCuenta().equals(numeroABuscar)) {
                return true;
            }
        }
        return false;
    }

    /**
     * EXTRA ÚTIL: Devuelve el objeto Cuenta directamente si el número coincide.
     * Esto te servirá para hacer ingresos o transferencias en el main.
     */
    public Cuenta obtenerCuenta(String numero) {
        for (int i = 0; i < numCuentaAsociadas; i++) {
            if (cuentas[i].dameCuenta().equals(numero)) {
                return cuentas[i];
            }
        }
        return null;
    }

    public boolean esMorosa() {
        for (int i = 0; i < numCuentaAsociadas; i++) {
            if (cuentas[i].consultar_saldo() < 0) {
                return true; 
            }
        }
        return false;
    }

    public String dameDni() {
        return dni; 
    }

    public String toString() {
        String cad = "DNI: " + dni + "\nCuentas asociadas (" + numCuentaAsociadas + "/3):\n";
        for (int i = 0; i < numCuentaAsociadas; i++) {
            cad += "  " + cuentas[i].toString() + "\n";
        }
        return cad;
    }

    public int maxcuentas() {
        return numCuentaAsociadas;
    }
}