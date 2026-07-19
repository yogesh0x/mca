import java.awt.*;
import java.awt.event.*;

//Out side of Class, implementation.

class event2 extends Frame {
	TextField t;
	event2 (){
        
        t = new TextField();
        t.setBounds(30,30,150,30);
        Button b = new Button("Click-Me");
        b.setBounds(30,70,50,20);

        Outer o = new Outer(this);
        b.addActionListener(o);
        add(t);
        add(b);

       setSize(555,555);
       setLayout(null);
       setVisible(true);


	}
	public static void main(String[] args){

	event2 os = new event2();
 }
	}
 class Outer implements ActionListener{

 	event2 a;
 	Outer(event2 a){
 		this.a = a;
 	}
public void actionPerformed(ActionEvent e){
		
		a.t.setText("Haha!");
	}
}