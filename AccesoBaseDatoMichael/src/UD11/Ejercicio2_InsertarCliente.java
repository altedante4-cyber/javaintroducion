package UD11;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class Ejercicio2_InsertarCliente {

    public static void main(String[] args) {
        String user = "admin";
        String contraseña = "1234";
        String uri = "jdbc:mysql://localhost:3306/bd_clientes";

        String nuevoNombre = "Juan";
        String nuevoApellido = "Perez";

        try (Connection connection = DriverManager.getConnection(uri, user, contraseña);
             PreparedStatement pstmt = connection.prepareStatement(
                     "INSERT INTO clientes (nombre, apellido) VALUES (?, ?)")) {

            System.out.println("Conexion establecida con exito.");

            pstmt.setString(1, nuevoNombre);
            pstmt.setString(2, nuevoApellido);

            int filas = pstmt.executeUpdate();
            System.out.println("Cliente insertado correctamente. Filas afectadas: " + filas);

        } catch (SQLException e) {
            System.out.println("Error de SQL: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Error general: " + e.getMessage());
        }
    }
}
