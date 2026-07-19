//"this" keyword used to call the current class method
class this2{
	void this2(){
		System.out.println("Method involved");
	}
	void p(){
		this.this2();
	}
}
class mthis2{
	public static void main(String[] args) {
		this2 t=new this2();
		t.p();
	}
}