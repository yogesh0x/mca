class cons3{
	int id;
	String name;
	cons3(int a,String n){  
		id = a ;
		name = n ;
	}
	void display(){
		System.out.println(name+" "+id);
	}
}
class mcons3{
	public static void main(String[] args) {
		cons3 c = new cons3(101,"Jack Sparrow");
		c.display();
	}
}