import java.awt.*;
import java.awt.event.*;


class mouse extends Frame implements MouseListener{

	Label l;
	mouse(){

		l = new Label("test");
		l.setBounds(50,50,100,20);
		l.addMouseListener(this);
		add(l);
		setSize(555,555);
		setLayout(null);
		setVisible(true);

	}
	public void mouseClicked(MouseEvent e){
		l.setText("Mouse CLicked");
	}
		public void mousePressed(MouseEvent e){
		l.setText("Mouse CLicked5");
	}
		public void mouseEntered(MouseEvent e){
		l.setText("Mouse CLicked2");
	}
		public void mouseReleased(MouseEvent e){
		l.setText("Mouse CLicked3");
	}
		public void mouseExited(MouseEvent e){
		l.setText("Mouse CLicked 4");
	}

	public static void main(String[] args){
		mouse m = new mouse();
	}
}