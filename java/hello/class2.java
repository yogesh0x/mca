public class class2 {
	double w, h, b;
	void volume () {
	System.out.println (w*h*b);
	}
}
class mclass2 {
	public static void main ( String[] args){
	class2 c1 = new class2();
	c1.h = 3 ;
	c1.w = 4 ;
	c1.b = 6 ;
	c1.volume();
	}
}