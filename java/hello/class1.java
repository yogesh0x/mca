public class class1 {
	double w, h, b;
}
class mclass1 {
	public static void main (String[] args) {
	class1 c1 = new class1();
	c1.w = 10 ;
	c1.h = 20 ;
	c1.b = 30 ;
	System.out.println ("Volume = " + c1.w*c1.h*c1.b);
	}
}