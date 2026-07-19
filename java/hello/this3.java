//"this()" call the current class constructor
class this3{
	this3(){
		int a;
		System.out.println("this is default constructor");
	}
	this3(int a){
this();
this.a=a;
System.out.println(a);
	}
}
class mt{
	public static void main(String[] args) {
		this3 t1=new this3(10);
		t1.this3();
	}
}