class cons2{
	int id;
	String name;
	cons2(){

		this.name = "Constructor";
		this.id = 10 ;
		System.out.println(name+" "+id);
	}
}
class mcons2{
	public static void main(String[] args) {
		cons2  c = new cons2();
	}
}
