public class copyarr {
  public static void main ( String args[] ) {
  int x [] = new int [] { 2, 4, 6, 8, 10, 12, 14, 16 };
  int y [] = new int [x.length];
  for (int i = 0; i < x.length; i++) {
  y[i] = x[i] ;
  }
  System.out.println ("Elements of x: ");
  for ( int i = 0; i < x.length; i++) {
  System.out.print(x[i] + " ") ;

  }
  System.out.println();
  System.out.println ("Elements of y: ");
  for ( int i = 0; i < y.length; i++ ) {
  System.out.print(y[i] + " ");
      }
    }
  }
