

class shape {
	public void area(){
		System.out.println("Displays Area: ");
	}
}

class triangle extends inh{
	public void area(int l, int h){
		System.out.println(1/2*l*h);
	}
}

 class ab {
 	int a = 1;
 	int b = 2;
 	double c = (double)a*b;
 	System.out.println(c);
 	 }

class inh {
	public static void main(String[] args){
		shape a = new shape();
		a.area();
	}
}