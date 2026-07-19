import java.awt.*;
import java.awt.event.*;


class event extends Frame implements ActionListener{
	
TextField tf ;

	event(){
      
      tf = new TextField();
      tf.setBounds(30,30,180,30);
      Button b = new Button("Click Me");
      b.setBounds(50,70,30,20);
      b.addActionListener(this);

      add(tf);
      add(b);


      setSize(444,444);
      setLayout(null);
      setVisible(true);

}
      public void actionPerformed(ActionEvent e){
      	tf.setText ("Welle-Comee!");
      }
      public static void main(String[] args){
      	event o = new event();
      }

	
}