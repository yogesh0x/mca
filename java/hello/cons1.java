public class cons1{
	void cons1(){
		System.out.println("This is a method");
	}
	cons1(){
		System.out.println("Hello, I am a Constructor :) ");
	}
}
 class mcons1{
	public static void main(String[] args) {
		cons1 a1 = new cons1();
		a1.cons1();
	}
}