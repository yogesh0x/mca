import java.awt.*;
import java.awt.event.*;

class Men extends Frame {
	
	Men(){

      MenuBar mb = new MenuBar();
      Menu m1 = new Menu("File");
      Menu m2 = new Menu("Edit");
      MenuItem mt1 = new MenuItem("Open");
      MenuItem mt2 = new MenuItem("Save"); 
      MenuItem mt3 = new MenuItem("Save As");
      MenuItem mt4 = new MenuItem("Copy");
      MenuItem mt5 = new MenuItem("Cut");
      MenuItem mt6 = new MenuItem("Paste");

      mb.add(m1);
      mb.add(m2);
      m1.add(mt1);
      m1.add(mt2);
      m1.add(mt3);
      m2.add(mt4);
      m2.add(mt5);
      m2.add(mt6);
     setMenuBar(mb);

   setSize(400, 300);
   setLayout(null);
   setVisible(true);

}

		public static void main(String[] args){
			Men mn = new Men();
		}
	
}