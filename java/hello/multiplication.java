public class multiplication {
	public static void main (String args[]) {
	int x[][] = {{1, 2, 3}, {2, 2, 2}};
	int y[][] = {{3, 3, 3}, {4, 4, 4}};
	int z[][] = new int [2][3];
	for (int a = 0; a < 2; a++) {
	for (int b = 0; b < 3; b++) {
	z [a][b] = 0;
	for (int k = 0; k < 3; k++) {
	z[a][b] += x[a][b] * y[a][b];
	
	}
	System.out.print(z[a][b] + " ");
	
   }
   System.out.println();
	}
  }
}