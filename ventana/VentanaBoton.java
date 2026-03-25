
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class VentanaBoton extends JFrame implements ActionListener {
    
    private JPanel panel;
    private JButton btn1 , btn2;

        public VentanaBoton(){
             panel = new JPanel();
             btn1 = new JButton("Boton1");
             btn2 = new JButton("Boton2");
             // añadimos  al panel
             panel.add(btn1);
             panel.add(btn2);
             this.add(panel);
             
             btn1.addActionListener(this);
             btn2.addActionListener(this);
             
             this.setSize(200,300);
             this.setLocation(200,200);
             this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
             this.setVisible(true);
        }
    

         @Override
          public void actionPerformed(ActionEvent e){
             if(e.getSource() == btn1){
                 System.out.println("has pulsado btn1 ");
             }else {
                    System.out.println("has pulsado boton2 ");
             }
        }
    
}
