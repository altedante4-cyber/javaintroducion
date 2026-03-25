
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class contador extends JFrame implements  ActionListener {
    
 private JPanel panel; 
    private JTextField campoTexto;
    private JButton boton;
    private JLabel etNombre;
    private JLabel saludo ; 
    private int contador = 0 ; 
    public contador(){
         //construimos las dimensiones de las ventanasa
        setTitle("Primera Ventana");
        setSize(300, 300);
        setLocation(100, 100);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

          // Creamos los componentes
        panel = new JPanel();
        campoTexto = new JTextField(20);
        boton = new JButton("Saluda");
        saludo = new JLabel("hola");

         boton.addActionListener(this);


          // Añadimos componentes al panel
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
     String nombre = campoTexto.getText();
        saludo.setText(nombre + contador );
     contador += 1 ; 
        System.out.println("Has pulsado el botón. Hola, " + nombre);
    }

}
