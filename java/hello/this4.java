class this4{
	int roll;
	String name;
	double fees;
	this4(int roll,String name){
		this.roll = roll;
		this.name = name;

	}
	this4(int roll,String name,double fees){
		this(roll,name);
		this.fees = fees;
		System.out.println(roll+" "+name+" "+fees);
	}
}
class mthis4{
	public static void main(String[] args) {
		this4 b = new this4(1,"xyz",1000);
		b.this4();
	}
}