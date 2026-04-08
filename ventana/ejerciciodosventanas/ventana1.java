package ejerciciodosventanas;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.* ;

public class ventana1 extends JFrame implements ActionListener {

    private JButton ventana1 , ventana2 ;
    private JPanel panel ; 
    private JPanel panel2 ; 
    public ventana1(){
        panel  = new JPanel();
        panel2 = new JPanel();
        
        ventana1 = new JButton("ir a ventana 2 ");
        ventana2 = new JButton("ir ventana 1");
        ventana1.addActionListener(this);
        ventana2.addActionListener(this);
        this.setSize(200,200);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        panel.add(ventana1);
        this.add(panel);
        this.setVisible(true);     
    }

    public void actionPerformed(ActionEvent e ){

        if (e.getSource() == ventana1) {
            ventana1.setVisible(false);

            this.setSize(200,200);
            this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            panel2.add(ventana2);
            this.add(panel2);
            this.setVisible(true);  
        }

        if(e.getSource() == ventana2){
            ventana2.setVisible(false);
            ventana1.setVisible(true);
        }
    }
     


    
}
