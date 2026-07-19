
/*class student{
	String name;
	int age;

	student(){

	System.out.println("Hello");
	}
}

class cons{
	public static void main(String [] args){

       student a = new student();
	}
}*/


/*class student{
    
     String name;
     int age;



       public void print(){
       	System.out.println(this.name);
       	System.out.println(this.age);
       }

     student( String nam, int ag){

     	this.name = nam;
     	this.age = ag;
     }
}

class cons {
	public static void main(String[] args){

		student a = new student("abcd", 10);
		a.print();
	}
}*/





//copy constructor

class student{

	String name;
	int age;


	void print(){
		System.out.println(this.name);
		System.out.println(this.age);
	}


	student(student s2){
		this.name = s2.name;
		this.age = s2.age;
	}

	student(){

	}
}


class cons{
	public static void main(String[] args){

         student s1 = new student();
         s1.name = "Haha";
         s1.age = 20;


         student s2 = new student(s1);
         s2.print();

	}
}