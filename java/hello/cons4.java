class cons4{
	int id;
	String name;
	cons4(int a,String n){
		id = a;
		name = n;
	}
	cons4(cons4 S){
		id = S.id;
		name = S.name;
	}
	void display(){
		System.out.println(name+" "+id);
	}
}
class mcons4{
	public static void main(String[] args) {             //copy constructor
		cons4 c = new cons4(707,"Doremon");
		cons4 c1 = new cons4(c);
		c.display();
		c1.display();
	}
}