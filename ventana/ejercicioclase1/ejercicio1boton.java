package ejercicioclase1;
import javax.print.DocFlavor.INPUT_STREAM;
import javax.swing.*;

import java.awt.Panel;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ejercicio1boton  extends JFrame  implements ActionListener {
     private JPanel panel ; 
     private JTextField num1 , num2  ; 
     private  JLabel texto1  , textoresultado;
    private JLabel texto2 ;
    private JButton btn1suma ,   btn2resta;
   

        public ejercicio1boton(){
             panel = new JPanel();
             texto1= new JLabel("Num1");
             num1 = new JTextField(12);
             texto2 = new JLabel("Num2");
             num2 = new JTextField(12);
             btn1suma = new JButton("SUMAR");
             btn2resta = new JButton("Restar");
             textoresultado = new JLabel();
          
             this.setSize(500,300);
             this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
             this.setLocation(200,200);


             btn1suma.addActionListener(this);
             btn2resta.addActionListener(this);
             

             panel.add(texto1);
             panel.add(num1);
             panel.add(texto2);
             panel.add(num2);
             panel.add(btn1suma);
             panel.add(btn2resta);
             panel.add(textoresultado);
            

             this.add(panel);
             this.setVisible(true);


        }

        public void actionPerformed(ActionEvent e ){
            int entero1 = Integer.parseInt(num1.getText());
             int entero2 = Integer.parseInt(num2.getText());
            
                if(e.getSource() == btn1suma ){
                 
            
                  int resultado = entero1 + entero2 ; 
                  textoresultado.setText(String.valueOf(resultado)); 
                }else{
                    int resultado2 = entero1 - entero2 ; 
                  textoresultado.setText(String.valueOf(resultado2)); 

                }
        } 


}
