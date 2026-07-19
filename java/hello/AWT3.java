import java.awt.*; // Correct import statement
import java.awt.event.*; // Import for handling events

class AWT3 extends Frame { // Class name should start with an uppercase letter
    AWT3() {
        // Create Labels and TextFields
        Label l = new Label("User Id");
        l.setBounds(50, 50, 80, 20);
        add(l); // Correctly add the label to the frame

        TextField tf1 = new TextField();
        tf1.setBounds(150, 50, 110, 20);
        add(tf1); // Correctly add the text field to the frame

        Label l1 = new Label("Password");
        l1.setBounds(50, 80, 80, 20);
        add(l1); // Correctly add the label to the frame

        TextField tf2 = new TextField();
        tf2.setBounds(150, 90, 110, 20);
        tf2.setEchoChar('*'); // Correct method name
        add(tf2); // Correctly add the text field to the frame

        Button b = new Button("Click");
        b.setBounds(150, 150, 60, 20);
        add(b); // Correctly add the button to the frame

        // Frame settings
        setSize(350, 350);
        setLayout(null);
        setVisible(true); // 'true' should be lowercase


    }

    public static void main(String[] args) {
        new AWT3(); // Create an instance of the AWT3 class
    }
}