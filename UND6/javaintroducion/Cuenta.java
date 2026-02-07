
package javaintroducion;
public class Cuenta {
    private double saldo;
    private String n_cuenta;

<<<<<<< HEAD
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
=======
    public Cuenta(String n_cuenta, double saldoInicial) {
        this.n_cuenta = n_cuenta;
        this.saldo = saldoInicial; // Ahora sí aceptamos un saldo inicial
    }

    public boolean recibirABonons(double cant) {
        if (cant > 0) {
>>>>>>> 7fb839fedeb3667b3e4e4a8fec21999d21a42ed1
            saldo += cant;
            return true;
        }
        return false;
    }

<<<<<<< HEAD
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
=======
    public boolean PagarRecibo(double cant) {
        // Verificamos que la cantidad sea positiva Y que tengamos dinero suficiente
        if (cant > 0 && saldo >= cant) {
            saldo -= cant;
            return true;
        }
        return false; // Retorna false si no hay dinero o la cantidad es inválida
    }

    @Override
    public String toString() {
        return "Cuenta: " + n_cuenta + " | Saldo: " + saldo;
>>>>>>> 7fb839fedeb3667b3e4e4a8fec21999d21a42ed1
    }
}