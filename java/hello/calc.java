import java.awt.*;
import java.awt.event.*;


class calc extends Frame implements MouseListener {
   


   

  TextField t;
  Button b1,b2,b3,b4,b5,b6,b7,b8,b9,b0,p,a,s,m,d,e;

  calc(){

  	t = new TextField();
  	t.setBounds(0,0,100,1000);

   b1 = new Button("1");
   b1.setBounds(110,50,20,20);
   b2 = new Button("2");
   b2.setBounds(10,50,20,20);
   b3 = new Button("3");
   b3.setBounds(10,50,20,20);
   b4 = new Button("4");
   b4.setBounds(10,50,20,20);
   b5 = new Button("5");
   b5.setBounds(10,50,20,20);
   b6 = new Button("6");
   b6.setBounds(10,50,20,20);
   b7 = new Button("7");
   b7.setBounds(10,50,20,20);
   b8 = new Button("8");
   b8.setBounds(10,50,20,20);
   b9 = new Button("9");
   b9.setBounds(10,50,20,20);
   b0 = new Button("0");
   b0.setBounds(10,50,20,20);
   p = new Button(".");
   p.setBounds(10,50,20,20);
   a = new Button("+");
   a.setBounds(10,50,20,20);
   s = new Button("-");
   s.setBounds(10,50,20,20);
   m = new Button("*");
   m.setBounds(10,50,20,20);
   d = new Button("\\");
   d.setBounds(10,50,20,20);
   e = new Button("=");
   e.setBounds(10,50,20,20);
   add(t);
 add(b1); 
 add(b2);
setSize(555,555);
setLayout(null);
setVisible(true);
  }
public void mouseClicked(MouseEvent e){
		t.setText("Mouse CLicked");
	}
		public void mousePressed(MouseEvent e){
		t.setText("Mouse CLicked5");
	}
		public void mouseEntered(MouseEvent e){
		t.setText("Mouse CLicked2");
	}
		public void mouseReleased(MouseEvent e){
		t.setText("Mouse CLicked3");
	}
		public void mouseExited(MouseEvent e){
		t.setText("Mouse CLicked 4");
	}
public static void main(String[] args){
	calc c = new calc();
}

}