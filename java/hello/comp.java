 public class comp{
 public static void main(String args[]){

 String x = "Hello";
 String y = "Hallo";
// Comparing exact string values
Boolean z = x.equals(y);
System.out.println(z);

String xx = "HELLO";
// Comparing with ignoring Case Sensetivity
Boolean zz = x.equalsIgnoreCase(xx);
System.out.println(zz);

//Comparing by how many numbers are differ each other by alphabetically
int zzz = x.compareTo(y);
System.out.println(zzz);

//== or reference comparision
String a = "hello";
String b = "hello"; 
// same string values which is stored in 'String constraint pool'
Boolean ab = (a == b);
System.out.println(ab); // true

// Not stores in that 
String c = new String ("hello");
String d = "hello";
Boolean cd = (c==d);
System.out.println(cd); //false


// String formatting method %d is for int, %s is for strings, %f is for floats;
String lan = "Java";
int marks = 99;

String form = String.format("The Students marks:%d of computer language:%s",marks,lan);
System.out.println(form);


 }
 }