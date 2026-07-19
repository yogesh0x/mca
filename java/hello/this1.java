//"this" keyword reffer to current class object
//"this" keyword always reffer to current class instance varriable
class this1{
	int roll;
	String name;
	this1(int roll,String name){
		this.roll = roll;
		this.name = name;
	}
	void display(){
		System.out.println(roll+" "+name);
	}
}
class mthis1 {
	public static void main(String[] args) {
		this1 t = new this1(101,"Rock Robin");
		t.display();
	}
}