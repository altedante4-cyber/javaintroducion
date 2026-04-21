import javax.swing.*;
import java.awt.*;

public class Estadisticas_Texto extends JFrame {

    private JTextField texto;
    private JLabel lblLetras, lblPalabras, lblEspacios, lblVocales, lblConsonantes;
    private JLabel numLetras, numPalabras, numEspacios, numVocales, numConsonantes;
    private JButton btnCalcular;

    public Estadisticas_Texto() {
        setTitle("Estadisticas de Texto");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());

        JLabel title = new JLabel("Escribe texto:");
        add(title);

        texto = new JTextField(25);
        add(texto);

        btnCalcular = new JButton("Calcular");
        add(btnCalcular);

        lblLetras = new JLabel("Numero de letras:");
        numLetras = new JLabel("0");
        lblPalabras = new JLabel("Numero de palabras:");
        numPalabras = new JLabel("0");
        lblEspacios = new JLabel("Numero de espacios:");
        numEspacios = new JLabel("0");
        lblVocales = new JLabel("Numero de vocales:");
        numVocales = new JLabel("0");
        lblConsonantes = new JLabel("Numero de consonantes:");
        numConsonantes = new JLabel("0");

        add(lblLetras);
        add(numLetras);
        add(lblPalabras);
        add(numPalabras);
        add(lblEspacios);
        add(numEspacios);
        add(lblVocales);
        add(numVocales);
        add(lblConsonantes);
        add(numConsonantes);

        btnCalcular.addActionListener(e -> actualizarEstadisticas());

        setVisible(true);
    }

    private void actualizarEstadisticas() {
        String textoActual = texto.getText();
        
        int letras = 0;
        int espacios = 0;
        int vocales = 0;
        int consonantes = 0;
        
        String vocalesStr = "aeiouAEIOU";
        
        for (int i = 0; i < textoActual.length(); i++) {
            char c = textoActual.charAt(i);
            if (Character.isLetter(c)) {
                letras++;
                if (vocalesStr.indexOf(c) >= 0) {
                    vocales++;
                } else {
                    consonantes++;
                }
            } else if (c == ' ') {
                espacios++;
            }
        }
        
        int palabras = 0;
        if (!textoActual.trim().isEmpty()) {
            String[] palabrasArray = textoActual.trim().split("\\s+");
            palabras = palabrasArray.length;
        }
        
        numLetras.setText(String.valueOf(letras));
        numPalabras.setText(String.valueOf(palabras));
        numEspacios.setText(String.valueOf(espacios));
        numVocales.setText(String.valueOf(vocales));
        numConsonantes.setText(String.valueOf(consonantes));
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new Estadisticas_Texto());
    }
}
