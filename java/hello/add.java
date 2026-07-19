public class add {
	public static void main ( String args[]) {
	int x[][] = {{2, 4, 6}, {1, 3, 5}};
	int y[][] = {{1, 2, 3}, {3, 6, 9}};
	int z[][] = new int [2][3];
	for (int i = 0; i < 2; i++)  {
	for (int j = 0; j < 3; j++) {
	z [i][j] = x[i][j] + y[i][j];
	System.out.print(z[i][j]+" ");
	}
	System.out.println();
	}
	}
}