
package javaintroducion;
public class Cuenta {
    private double saldo;
    private String n_cuenta;

    public Cuenta(String n_cuenta, double saldoInicial) {
        this.n_cuenta = n_cuenta;
        this.saldo = saldoInicial; // Ahora sí aceptamos un saldo inicial
    }

    public boolean recibirABonons(double cant) {
        if (cant > 0) {
            saldo += cant;
            return true;
        }
        return false;
    }

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
    }
}