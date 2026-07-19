// this:pass the argument in constructor call
class this6{
	B b1;
	this6(B b1){
		this.b1 = b1;
	}
	void display(){
		System.out.println(b1.data);
	}
}
class B{
	int data = 50;
	B(){
		this6 a1 = new this6(this);
		a1.display();
	}
}
class mthis6{
	public static void main(String[] args) {
		B b1 = new B();
	}
}