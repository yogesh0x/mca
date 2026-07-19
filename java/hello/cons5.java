class cons5{
	int id;
	String name;
cons5(int i,String n){
	 id = i;
	name = n ;
}
cons5(){}
void display(){
	System.out.println(id+" "+name);
}
}
class mcons5{
	public static void main(String[] args) {
		cons5 c = new cons5(151,"Iron Man");
		cons5 c1 = new cons5();
		c1.id = c.id;
		c1.name = c.name;
		c.display();
		c1.display();
	}
}