public class conc{
	public static void main(String[] args){
	String x = "Text";
	String y = "Box";
	 String xy = x+" "+y;
	 System.out.println(xy);
	 String xy2 = x.concat(" ").concat(y);
	 System.out.println(xy2);
	 int len = xy.length();
	 System.out.println(len);
	 String substr = xy.substring(5);
	 System.out.println(substr);
	}
}
