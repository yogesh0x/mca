// Single Inheritance 1
class inher1{
	int i,j;
	void show(){
		System.out.println(i+" "+j);

	}
}
class in extends inher1{
	int k = 40;
	void add(){
		System.out.println(i+j+k);
	}
}
class Minher1{
	public static void main(String[] args) {
		in n = new in();
		n.i = 10;
		n.j = 30;
		n.show();
		n.add();
	}
}