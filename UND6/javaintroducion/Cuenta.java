package javaintroducion;

public class Cuenta {
    private double saldo;
    private String n_cuenta;

    // Constructor con saldo inicial
    public Cuenta(String n_cuenta, double saldoInicial) {
        this.n_cuenta = n_cuenta;
        this.saldo = saldoInicial;
    }

    // Constructor por defecto (saldo 0)
    public Cuenta(String n_cuenta) {
        this.n_cuenta = n_cuenta;
        this.saldo = 0.0;
    }

    // Para que la clase Persona pueda leer el número de cuenta y comparar
    public String dameCuenta() {
        return n_cuenta;
    }

    public double consultar_saldo() {
        return saldo;
    }

    // Método para ingresar dinero
    public boolean recibirABonons(double cant) {
        if (cant > 0) { 
            saldo += cant;
            return true;
        }
        return false;
    }

    // Método para retirar dinero o pagar recibos
    public boolean PagarRecibo(double cant) {
        // Validamos que la cantidad a quitar sea positiva 
        // y (opcionalmente) que no se quede el saldo excesivamente negativo
        if (cant > 0) {
            saldo -= cant;
            return true;
        }
        return false;
    }

    public String toString() {
        return "[Cuenta: " + n_cuenta + " | Saldo: " + saldo + "€]";
    }
}