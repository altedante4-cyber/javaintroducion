package ejercicio4ventana;
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;
public class ejercicio4 extends JFrame implements  ActionListener {
    private JFrame ventana;
    private JPanel panel ;
    private JLabel usuario , mostrarnumero ; 
    private JButton btnmayor , btnmenor , btnacertado ;
    private Random rand = new Random() ;
    private int numeroelegido ;
    public ejercicio4(){
        
        panel = new JPanel();
         mostrarnumero = new JLabel();
        btnmayor = new JButton("Mayor");
        btnmenor = new JButton("Menor");
        btnacertado = new JButton("Acertado");
        numeroelegido = rand.nextInt(0,100);    
        this.setSize(200,200);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        btnmayor.addActionListener(this);
        btnmenor.addActionListener(this);
        btnacertado.addActionListener(this);
        panel.add(btnmayor);
        panel.add(btnmenor);
        panel.add(btnacertado);
        panel.add(mostrarnumero);
        this.add(panel);
        mostrarnumero.setText(String.valueOf("el numero es "  + numeroelegido));
     
        this.setVisible(true);

    }

    @Override
    public void actionPerformed(ActionEvent e ){
         
            if(e.getSource() == btnmayor){
                    numeroelegido = rand.nextInt( numeroelegido , 100);
                    mostrarnumero.setText(String.valueOf("el numero es "  + numeroelegido));
          
            }else if (e.getSource() == btnmenor ){
                    numeroelegido = rand.nextInt(0,numeroelegido);
                    mostrarnumero.setText(String.valueOf("el numero es "  + numeroelegido));

                  
            }else{
                       mostrarnumero.setText("acertado");

                  
            }
    

    }

}
