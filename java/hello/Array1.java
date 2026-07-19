public class Array1 {
	public static void main ( String[] args) {
	int marks [] = { 75, 80, 79, 78, 85};
	//  
	int sum = 0;
	for ( int i = 0; i < marks.length; i++){
		sum = sum + marks[i];
		
		/*System.out.println(sum);*/
		

	} 
	double avg = sum / marks.length;
	System.out.println(avg);
  }
}