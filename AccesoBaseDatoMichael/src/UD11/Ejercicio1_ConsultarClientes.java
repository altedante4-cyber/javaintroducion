package UD11;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Ejercicio1_ConsultarClientes {

    public static void main(String[] args) {
        String user = "admin";
        String contraseña = "1234";
        String uri = "jdbc:mysql://localhost:3306/bd_clientes";

        try (Connection connection = DriverManager.getConnection(uri, user, contraseña);
             Statement statement = connection.createStatement()) {

            System.out.println("Conexion establecida con exito.");

            String sql = "SELECT * FROM clientes";
            ResultSet rs = statement.executeQuery(sql);

            System.out.println("Listado de clientes:");
            System.out.println("-------------------");
            while (rs.next()) {
                int id = rs.getInt("id");
                String nombre = rs.getString("nombre");
                String apellido = rs.getString("apellido");
                System.out.println(id + " | " + nombre + " " + apellido);
            }

        } catch (SQLException e) {
            System.out.println("Error de SQL: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Error general: " + e.getMessage());
        }
    }
}
