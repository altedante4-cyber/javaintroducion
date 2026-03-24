import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

// Implementamos ActionListener para capturar el click
public class ventana1 extends JFrame implements ActionListener {
    
    private JPanel panel; 
    private JTextField campoTexto;
    private JButton boton;
    private JLabel etNombre;
    private JLabel saludo ; 
    public ventana1() {
        // Configuramos la ventana actual (this)
        setTitle("Primera Ventana");
        setSize(300, 300);
        setLocation(100, 100);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Creamos los componentes
        panel = new JPanel();
        etNombre = new JLabel("Nombre:");
        campoTexto = new JTextField(20);
        boton = new JButton("Saluda");
        saludo = new JLabel("hola");
        // Agregamos el Listener al botón
        // "this" se refiere a esta misma clase que tiene el método actionPerformed
        boton.addActionListener(this);

        // Añadimos componentes al panel
        panel.add(etNombre);
        panel.add(campoTexto);
        panel.add(boton);
        panel.add(saludo);
        // Vinculamos el panel a la ventana
        this.setContentPane(panel);
        
        // Hacemos visible
        this.setVisible(true);
    }

    @Override 
    public void actionPerformed(ActionEvent e) {
        // Ahora además de la consola, podemos interactuar con el campo de texto
        String nombre = campoTexto.getText();
        saludo.setText(nombre);
        System.out.println("Has pulsado el botón. Hola, " + nombre);
    }

   
}