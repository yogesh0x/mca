// this: pass the argument in method call
class this5{
	void this5(this5 obj){
		System.out.println("With Method");
	}
	void p(){
		this5(this);
	}
}
class mthis5{
	public static void main(String[] args) {
		this5 a = new this5();
		a.p();
	}
}