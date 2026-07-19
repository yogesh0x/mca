import java.awt.*;
import java.awt.event.*;


class choice extends Frame{

	choice(){
	Choice c = new Choice();
     c.add("Jan");
     c.add("Feb");
     c.add("Mar");
     
     c.setBounds(20,50,60,40);


     add(c);

      setSize(500,500);
      setLayout(null);
      setVisible(true);

	}

public static void main (String[] args){
	choice choice = new choice();
}

}