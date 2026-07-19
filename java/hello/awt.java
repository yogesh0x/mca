import java.awt.*;
import java.awt.event.*;
class awt extends Frame implements ActionListener {

     Label l, l2, l3, l4, l5;
     TextArea tA, tA2;
     TextField tF, tF2;
     Button b;
     Checkbox cb,cb1,cb2,cb3;
     CheckboxGroup cbg;
    


	awt() {

         /*l = new Label ("Abstract Window Toolkit");
         l.setBounds(20,40,120,20);
         add(l);
         tA = new TextArea ("Text area is here!");
         tA.setBounds(20,70,250,50);
         add(tA);
         tF = new TextField("Text Field to Enter Texts");
         tF.setBounds(20,140,200,30);
         add(tF);
         b = new Button("I'm Button!");
         b.setBounds(20,180,80,25);
         add(b);*/

         l = new Label ("Sign Up Form!");
         l2 = new Label ("User Id:");
         l3 = new Label ("Password:");
         l4 = new Label ("Gender:");
         
         tF = new TextField();
         tF2 = new TextField();
         
         cbg = new CheckboxGroup();
         
         b = new Button("Sign up");
         l.setBounds(120,40,80,20);
         l2.setBounds(20,80,70,20);
         l3.setBounds(20,110,70,20);
        l4.setBounds(20,140,60,20);
         tF.setBounds(30,80,170,20);
         tF2.setBounds(30,110,170,20);
         tF2.setEchoChar('*');
        cb1 = new Checkbox("M",cbg,false);
         cb1.setBounds(90,145,40,10);
         cb2 = new Checkbox("F",cbg,false);
         cb2.setBounds(130,145,40,10);
         cb3 = new Checkbox("O",cbg,false);
         cb3.setBounds(180,145,40,10);
         b.setBounds(50,200,50,20);
         add(l);
         add(l2);
         add(l3);
         add(l4);
          add(cb1);
        add(cb2);
        add(cb3);
         add(tF);
         add(tF2);
         add(b);
  
    setSize(500, 500);
    setLayout(null);
    setVisible(true);
	}
	public void actionPerformed(ActionEvent e){

	}
	 
    public static void main(String[] args) {
        awt awt = new awt();
    }
}
