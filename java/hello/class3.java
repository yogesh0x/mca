public class class3 {
	double w, h, b;
	double volume (){
	return w * h * b;
 }
}
class mclass3 {
	public static void main( String[] args) {
	class3 c1, c2 ;
	class3 c1 = new class3();
	class3 c2 = new class3();

	c1.h = 15 ;
	c1.w = 25 ;
	c1.b = 25 ;
	System.out.println(c1.volume());
	}
}

/*public class Class3 {
  double w, h, b;
  double volume() {
    return w * h * b;
  }
}

public class Main {
  public static void main(String[] args) {
    Class3 c1 = new Class3();
    Class3 c2 = new Class3();
    c1.h = 15;
    c1.w = 25;
    c1.b = 25;
    System.out.println(c1.volume());
  }
}*/