package calculadora;
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class calculadora  extends JFrame implements ActionListener {
    
    private JFrame ventana;
    private JPanel panel ;
    private JTextField pantalla ;
    private JTextField resultado ;
    private JButton boton [] = new JButton[10] ;
    private int numero ;

    public calculadora(){

        panel = new JPanel();
        pantalla = new JTextField(12);
        resultado = new JTextField(12);
        panel.add(pantalla);
        panel.add(resultado);
        numero =  0 ;

        for (int i = 0 ; i < boton.length ; i++){
                boton[i] = new JButton(String.valueOf(i));
                panel.add(boton[i]);
                boton[i].addActionListener(this);
            }        



        this.setSize(200,200);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);          
        this.add(panel);
        this.setVisible(true);
        }


    public void actionPerformed(ActionEvent e ){
    }
    
}
